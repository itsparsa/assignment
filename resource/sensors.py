from datetime import datetime,timedelta

from flask.views import MethodView
from flask_smorest import Blueprint,abort
from sqlalchemy.exc import SQLAlchemyError,IntegrityError
from sqlalchemy import func


from models.sensors import SensorModel
from schema import SensorSchema,DesiredoutputSchema
from db import db

blueprint = Blueprint("sensor", __name__, description="Operation")
    

@blueprint.route('/sensor')
class Sensorlist(MethodView):

    @blueprint.response(200,SensorSchema(many=True))
    def get(self):
        return SensorModel.query.all()

    @blueprint.arguments(SensorSchema)
    @blueprint.response(200,SensorSchema)
    def post(self,new_sensor):
        new_sensor["timestamp"] = new_sensor["timestamp"] or datetime.datetime.now()
        new_sensor["measurement_type"] = new_sensor["measurement_type"].lower()
        sensor = SensorModel(**new_sensor)
        try:
            db.session.add(sensor)
            db.session.commit()
        except IntegrityError as e:
            abort(404,f"a data for sensor = {new_sensor['id']} \
                        with timestamp = {new_sensor['timestamp']} is already posted")     
        except SQLAlchemyError as e:
            abort(404,f"{e}")  
        return sensor    


@blueprint.route('/sensor/<int:id_value>/<string:measurement_type>/<string:duration>/<string:startdatetime>')
class Sensorlist(MethodView):
    @blueprint.response(200,DesiredoutputSchema)
    def get(self,id_value,measurement_type,duration,startdatetime):
        duration_type = ["1h","5min"] 
        if duration.lower() in ["1h","5min"] :
            duration = timedelta(minutes=5) if duration.lower() == "5min" else timedelta(hours=1)
        else :
            abort(404,message= f"Invalid duration. duration must be one of '{(' , ').join(duration_type)}' .") 

        startdatetime = datetime.fromisoformat(startdatetime)
        sensors = db.session\
                    .query( func.min(SensorModel.value).label("min"),
                            func.max(SensorModel.value).label("max"),
                            func.avg(SensorModel.value).label("mean"),
                            func.array_agg(SensorModel.timestamp).label("timestamps") )\
                    .where( SensorModel.id == id_value ,
                            SensorModel.measurement_type == measurement_type.lower(),
                            SensorModel.timestamp >= startdatetime,
                            SensorModel.timestamp <= startdatetime+duration)\
                    .all()[0]           

        return {"MIN_VALUE" : sensors[0],
                "MAX_VALUE" : sensors[1],
                "MEAN_VALUE" : sensors[2],
                "timestamps" : sensors[3]}


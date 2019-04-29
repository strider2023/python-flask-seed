from flask import Blueprint, jsonify
from dao.user_dao import UserDao
from database.user_queries import UserQueries

users_api = Blueprint('users_api', __name__)

db = UserQueries()

@users_api.route("/users", methods=["GET"])
def getEmployee():
    employees = []
    for x in db.getUsers():
        employee = UserDao(x[0], x[4], x[6])
        employees.append(employee.getEmployee())
    return jsonify({'users': employees})

# @users_api.route('/employee/<empId>',methods=['GET'])
# def getEmp(empId):
#     usr = [ emp for emp in empDB if (emp['id'] == empId) ]
#     return jsonify({'emp':usr})
#
# @users_api.route('/employee/<empId>',methods=['PUT'])
# def updateEmp(empId):
#     em = [ emp for emp in empDB if (emp['id'] == empId) ]
#     if 'name' in request.json :
#         em[0]['name'] = request.json['name']
#     if 'title' in request.json:
#         em[0]['title'] = request.json['title']
#     return jsonify({'emp':em[0]})
#
# @users_api.route('/employee/add',methods=['POST'])
# def createEmp():
#     dat = {
#     'id':request.json['id'],
#     'name':request.json['name'],
#     'title':request.json['title']
#     }
#     empDB.append(dat)
#     return jsonify(dat)
#
# @users_api.route('/employee/<empId>',methods=['DELETE'])
# def deleteEmp(empId):
#     em = [ emp for emp in empDB if (emp['id'] == empId) ]
#     if len(em) == 0:
#        abort(404)
#     empDB.remove(em[0])
#     return jsonify({'response':'Success'})

from flask import Blueprint, jsonify
from dao.employee import Employee

employees_api = Blueprint('employees_api', __name__)

@employees_api.route("/employees", methods=["GET"])
def getEmployee():
    employees = [];
    for index in range(3):
        employee = Employee(index, "Arindam", "Tech")
        employees.append(employee.getEmployee())
    return jsonify({'employees': employees})

# @employees_api.route('/employee/<empId>',methods=['GET'])
# def getEmp(empId):
#     usr = [ emp for emp in empDB if (emp['id'] == empId) ]
#     return jsonify({'emp':usr})
#
# @employees_api.route('/employee/<empId>',methods=['PUT'])
# def updateEmp(empId):
#     em = [ emp for emp in empDB if (emp['id'] == empId) ]
#     if 'name' in request.json :
#         em[0]['name'] = request.json['name']
#     if 'title' in request.json:
#         em[0]['title'] = request.json['title']
#     return jsonify({'emp':em[0]})
#
# @employees_api.route('/employee/add',methods=['POST'])
# def createEmp():
#     dat = {
#     'id':request.json['id'],
#     'name':request.json['name'],
#     'title':request.json['title']
#     }
#     empDB.append(dat)
#     return jsonify(dat)
#
# @employees_api.route('/employee/<empId>',methods=['DELETE'])
# def deleteEmp(empId):
#     em = [ emp for emp in empDB if (emp['id'] == empId) ]
#     if len(em) == 0:
#        abort(404)
#     empDB.remove(em[0])
#     return jsonify({'response':'Success'})

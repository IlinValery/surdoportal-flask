from application.gateway.department_gateway import DepartmentGateway


class ViewerService:

    @staticmethod
    def department_get_all():
        department_db = DepartmentGateway()
        rv = department_db.read_all()
        if rv==None:
            return {}
        else:
            return rv

    @staticmethod
    def department_get_by_id(dep_id):
        department_db = DepartmentGateway()
        rv = department_db.read_by_id(dep_id)
        return rv



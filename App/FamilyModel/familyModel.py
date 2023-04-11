from .familyDbModel import Family


class FamilyModel:

    @staticmethod
    def family_mem(f_id, f_name):
        """

        :param f_id:
        :param f_name:
        :return:
        """
        if f_id:
            family_mem = Family.query.filter_by(id=f_id).all()
        elif f_name:
            family_mem = Family.query.filter_by(name=f_name).all()
        else:
            return []
        return family_mem

from rolepermissions.roles import AbstractUserRole


class radicacion(AbstractUserRole):
    available_permissions = {
        'Radicar': True,
    }


class alistamiento(AbstractUserRole):
    available_permissions = {
        'Alistar': True,
    }


class Estructuracion(AbstractUserRole):
    available_permissions = {
        'Estructurar': True,
    }


class numeracion(AbstractUserRole):
    available_permissions = {
        'numerar': True,
    }


class secop_publicar(AbstractUserRole):
    available_permissions = {
        'secop_publicar': True,
    }


class secop_flujos(AbstractUserRole):
    available_permissions = {
        'secop_flujos': True,
    }


class tramite_crp(AbstractUserRole):
    available_permissions = {
        'tramite_crp': True,
    }


class financiera(AbstractUserRole):
    available_permissions = {
        'financiera': True,
    }
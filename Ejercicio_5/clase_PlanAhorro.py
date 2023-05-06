class PlanAhorro():
    cant_cuotas = 12
    cant_cuotas_pagas = 6
    def __init__(self, codigo = 0, modelo = " ", version_vehiculo = " ", valor_vehiculo = 0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version_vehiculo = version_vehiculo
        self.__valor_vehiculo = valor_vehiculo
    
    def importeCuota(self):
        return((self.__valor_vehiculo/self.get_cantidad_licitar()) + self.__valor_vehiculo * 0.10)
    
    def mostrar(self):
        print(self.__codigo, " ", self.__modelo, " ", self.__version_vehiculo)
    
    def set_valor(self, cantidad):
        self.__valor_vehiculo = cantidad
    
    @classmethod
    def get_cantidad_licitar(cls):
        return cls.cant_cuotas
    
    @classmethod
    def get_cantidad_cuotas(cls):
        return cls.cant_cuotas_pagas
    
    @classmethod 
    def set_cantidad_licitar(cls, cantidad):
        cls.cant_cuotas = cantidad

    
    @classmethod
    def set_cantidad_cuotas(cls, cantidad):
        cls.cantidad_cuotas_pagas = cantidad
    
    def get_codigo(self):
        return self.__codigo
    
import abc

class sysUserInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getSysUser():
        return NotImplemented
    
    @abc.abstractmethod
    def getSysUserById():
        return NotImplemented
    
    @abc.abstractmethod
    def addSysUser():
        return NotImplemented
    
    @abc.abstractmethod
    def delSysUser():
        return NotImplemented

    @abc.abstractmethod
    def validate():
        return NotImplemented
    

class testt(sysUserInterface):
    pass
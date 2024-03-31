from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BankRequest(_message.Message):
    __slots__ = ("branchID",)
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    branchID: int
    def __init__(self, branchID: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCashRequirementResponse(_message.Message):
    __slots__ = ("branchMinCash",)
    BRANCHMINCASH_FIELD_NUMBER: _ClassVar[int]
    branchMinCash: int
    def __init__(self, branchMinCash: _Optional[int] = ...) -> None: ...

class TotalEmployeesResponse(_message.Message):
    __slots__ = ("total_employees",)
    TOTAL_EMPLOYEES_FIELD_NUMBER: _ClassVar[int]
    total_employees: int
    def __init__(self, total_employees: _Optional[int] = ...) -> None: ...

class Employee(_message.Message):
    __slots__ = ("employee_id", "name", "branchID")
    EMPLOYEE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    employee_id: str
    name: str
    branchID: str
    def __init__(self, employee_id: _Optional[str] = ..., name: _Optional[str] = ..., branchID: _Optional[str] = ...) -> None: ...

class EmployeeResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class EmployeeID(_message.Message):
    __slots__ = ("employee_id",)
    EMPLOYEE_ID_FIELD_NUMBER: _ClassVar[int]
    employee_id: str
    def __init__(self, employee_id: _Optional[str] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class BranchInfo(_message.Message):
    __slots__ = ("branchID",)
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    branchID: str
    def __init__(self, branchID: _Optional[str] = ...) -> None: ...

class CashResponse(_message.Message):
    __slots__ = ("branchMinCash",)
    BRANCHMINCASH_FIELD_NUMBER: _ClassVar[int]
    branchMinCash: float
    def __init__(self, branchMinCash: _Optional[float] = ...) -> None: ...

class CashUpdateRequest(_message.Message):
    __slots__ = ("branchID", "branchMinCash")
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    BRANCHMINCASH_FIELD_NUMBER: _ClassVar[int]
    branchID: str
    branchMinCash: float
    def __init__(self, branchID: _Optional[str] = ..., branchMinCash: _Optional[float] = ...) -> None: ...

class CashUpdateResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class Client(_message.Message):
    __slots__ = ("client_id", "name", "branchID")
    CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    client_id: str
    name: str
    branchID: str
    def __init__(self, client_id: _Optional[str] = ..., name: _Optional[str] = ..., branchID: _Optional[str] = ...) -> None: ...

class Branch(_message.Message):
    __slots__ = ("location", "number_of_employees")
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_EMPLOYEES_FIELD_NUMBER: _ClassVar[int]
    location: str
    number_of_employees: int
    def __init__(self, location: _Optional[str] = ..., number_of_employees: _Optional[int] = ...) -> None: ...

class BranchResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UpdateBranchSizeRequest(_message.Message):
    __slots__ = ("branchID", "newNumberOfEmployees")
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    NEWNUMBEROFEMPLOYEES_FIELD_NUMBER: _ClassVar[int]
    branchID: int
    newNumberOfEmployees: int
    def __init__(self, branchID: _Optional[int] = ..., newNumberOfEmployees: _Optional[int] = ...) -> None: ...

class BankAllAtributesResponse(_message.Message):
    __slots__ = ("branchID", "branchSize", "branchLocation", "branchMinCash")
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    BRANCHSIZE_FIELD_NUMBER: _ClassVar[int]
    BRANCHLOCATION_FIELD_NUMBER: _ClassVar[int]
    BRANCHMINCASH_FIELD_NUMBER: _ClassVar[int]
    branchID: int
    branchSize: int
    branchLocation: str
    branchMinCash: int
    def __init__(self, branchID: _Optional[int] = ..., branchSize: _Optional[int] = ..., branchLocation: _Optional[str] = ..., branchMinCash: _Optional[int] = ...) -> None: ...

class BranchesResponseAll(_message.Message):
    __slots__ = ("branches",)
    BRANCHES_FIELD_NUMBER: _ClassVar[int]
    branches: _containers.RepeatedCompositeFieldContainer[BankAllAtributesResponse]
    def __init__(self, branches: _Optional[_Iterable[_Union[BankAllAtributesResponse, _Mapping]]] = ...) -> None: ...

class UpdateBranchSizeResponse(_message.Message):
    __slots__ = ("branchID", "branchMinCash", "branchLocation")
    BRANCHID_FIELD_NUMBER: _ClassVar[int]
    BRANCHMINCASH_FIELD_NUMBER: _ClassVar[int]
    BRANCHLOCATION_FIELD_NUMBER: _ClassVar[int]
    branchID: int
    branchMinCash: int
    branchLocation: str
    def __init__(self, branchID: _Optional[int] = ..., branchMinCash: _Optional[int] = ..., branchLocation: _Optional[str] = ...) -> None: ...

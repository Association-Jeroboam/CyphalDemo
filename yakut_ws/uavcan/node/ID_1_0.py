# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/node/ID.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:57.241072 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.ID
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class ID_1_0:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    def __init__(self,
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.node.ID.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint16 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint16 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 65535]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u16(max(min(self.value, 65535), 0))
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.node.ID.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> ID_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_u16()
        self = ID_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.node.ID.1.0'
        assert isinstance(self, ID_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.ID.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8jkSbg0{?YWO-~d-5M7i7TofS?FCJ_!1`m$nNiQB`V?tJN1IW#EdZuf4I_c@2^vAMeLLvu^B%NqN`+NLrR_}s~80IqFQ&q3('
        'y?XOy{@3gI*5nC~>V{h`Git#ICdFr#OUP)Ut6E#(AclJf&iKN41BXow@jN~~jVEz4w5ehh##cNW6-;GHbI5kOF)Yy$7%Q}jWh*Qm'
        'U7XKjZ?4z+7EfbXrp!4ba__*#Pw}Q1{wBrHekVZkS?><z%rWZHKsS}wMpVLy5oWA^R8|ZX@Ezq~2<BfR%QP2`N>D>r#@;G|7tA_Z'
        'A)i=oga`dgpj4J^V{A8tkWlMu+>c>{TE`S;hF=Bx?(?!8+9M`CPB2foE@Eg!pR=%jg+I-ksg5VHB;}gLX*kpd3g&>vv#>%3Vho(t'
        '+BhnB+zV^eYHtd_fCO4I>=hQ%ONu;(JAGW+xSzhBBe%Kd*t^tePq%6jLub3GOD4Ne=@=f?K9{1P28Ldyelt~V3=7k}Vtv{yZf&QV'
        'ZDlXAq;+(O_&P0_#R&{3m&6~50^(WuIQ;IyKq#<;kyQH(D?5iJkcy2(<tu`s2u>!_5Mc=t2E`GCXhj_6dAu3f2sI?mFl7^YB3T0_'
        '>l~#jOQb#qgUL*ht(UI|&On$vW{tf7A83Og<gDIioqZUj8a?S@YbeA(pw8&dNqVIbM5uwz(!O$u8a%nQ)@-pz)Lp;FaQCfn?<e;I'
        'yk1x<+@`vYf!qXQn=041090}p7lOu3vwWz*FsIGTpbNAp1=_!S6YlpJ=cvnnN#%Bm?s+MhX|6{RVd}#lakIDj)8_b()>EL^Tk<*5'
        't%OS6#{(Ou!(#G3x*}C~D2!{AG5yASKDW8gvp?%HoaICW000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

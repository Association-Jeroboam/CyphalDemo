# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/node/port/SubjectID.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.214881 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.port.SubjectID
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class SubjectID_1_0:
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
    MAX: int = 8191

    def __init__(self,
                 value: None | int | _np_.uint16 = None) -> None:
        """
        uavcan.node.port.SubjectID.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated uint13 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated uint13 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 8191:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 8191]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(max(min(self.value, 8191), 0), 13)
        _ser_.pad_to_alignment(8)
        assert 16 <= (_ser_.current_bit_length - _base_offset_) <= 16, \
            'Bad serialization of uavcan.node.port.SubjectID.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> SubjectID_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(13)
        self = SubjectID_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 16 <= (_des_.consumed_bit_length - _base_offset_) <= 16, \
            'Bad deserialization of uavcan.node.port.SubjectID.1.0'
        assert isinstance(self, SubjectID_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.node.port.SubjectID.1.0({_o_0_})'

    _EXTENT_BYTES_ = 2

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YW-)j>=5Kd{5rmd;gl!6s)DkyEi)4tV5Z7G!48k#D;$g+Dk$*x@Pj@`YG2!ef3C@d&+{C}Oz&$iNg*}468zWrwA'
        '+aJZhx>y)~ZZjK1CW-@QKr0@rZ(PI>urTdrsZkctRa;i)q0Kd%4>G_j+_}K-xa~?T;a$Qva^4Gh5+rE^L6&M8v~uwkLVJ9OuEKht'
        'jY<=g1-I~N9A9B$u2J}f7wDE5w^l2WTQK;AXzvg-J%z4xq#%xFLY7#>EoauNyDL4@s;jK((TUo}#HdaJ(Q#s-1NvrF%S<TCVn{kx'
        'VxvmrAvczFsW_BtZoN4n@@c^VVJ9A<iV8pR4BZ+tmM0O{(RHHBT*#6u^?00<f+CC35M2Rjcg0l>(!}T3sR&t<>*MHAqbfJ#Q@J@}'
        'm_K>@8ReFI=E`hL_GD5p^fL{{_xDD*l{0Q>kH-^wx$73&numVZ5Pmd{33tW)y*GR43o#-W;A+>V!^B`Taj&Z`SLKd;o>RXfpnF4Z'
        'A;L?y!rH125%WG^D#BB@%1oN;5D18YWt_U<7W@(`fo`!$F6%e_?iF=^?iFc}skc?x(#lETd`DSyO9z8Y^7s(CDZ0m5E@Blj4V^sp'
        'H_seE3FVO?iOE}%7B2?f!>KKUz2J4=n}*hpti~iaq)bC%y={6b1iX}6ZhxHdl2YpD66%^K9WZq|S&yKt$U}88s9Qoz2BB)JaM<g>'
        'k66Sc<;7$;GcV8$_Vz!zd+(HeKm2dO)Cg{#r5U>VT_k4E6)E+BN;sjukk|d~A2QI~rh4Y-G7F`m7b9Elev?O$N;>}?lAk?#n#VEM'
        'gWIUw{f*m=>K`NML1!ZdY*cbVb#_&PjR!v9eIG3Nw?b3#`j@;Zc`|(Sr@8Q+3jP5ZBzCKP1ONa'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

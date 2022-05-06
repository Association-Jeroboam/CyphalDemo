# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/primitive/scalar/Integer32.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.294438 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.primitive.scalar.Integer32
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
class Integer32_1_0:
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
                 value: None | int | _np_.int32 = None) -> None:
        """
        uavcan.primitive.scalar.Integer32.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated int32 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        saturated int32 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.int32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if -2147483648 <= x <= 2147483647:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [-2147483648, 2147483647]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_i32(max(min(self.value, 2147483647), -2147483648))
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.primitive.scalar.Integer32.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Integer32_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_i32()
        self = Integer32_1_0(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.primitive.scalar.Integer32.1.0'
        assert isinstance(self, Integer32_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.primitive.scalar.Integer32.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YWO>Yx15KWaPDJ>r=t+;R?<$%g%`T7A!v_e9mB_fC$vh4K`Tk`H&{)iH!O7sAtk|mHj{0ROf<ECvwQTJkd$MfdB'
        'dE>9EzyGvbXJ2|?XVObkFb__1qrY%rpkQTF*~aStm~M@Ni)DxoKFloODLy{NBiv0LR`ZJDJCRRHUKiHsN(ViG!k64|SG=hMjKRHl'
        'j%kfez<J%&s9LG_@qB-ZgOx$+J04@&U_1n;MGWBa6JAH_@)D-bYYj#&=&Uoz17{&~ye|EcBBsre9@ikxIsU6`g9#m&fqEPi4*CRL'
        'avxaLNI<on?hP+sa$2!Rv4b2UIjwK_9@94Sf!C5dxeW9p3e`!S2{)1IuQJ(`m|7SGPg_gsnV8KRdxWa5Ha)SCU>%e^fW(t@n|;<('
        'kjyqNFfH*gZ8G0PR{{kLFw3b{>gB~~f$7GOe4GyR-&4}I@`P%uCL7lcv~rKBJ=Ou!`rgbcZuX&SFx|IN7+o?4<7jf_MRzHoJGY#`'
        'mpa;=+m7k(rSZkH;%SkMz>xd0#T55M&_NxtGZS3`o~Rx5klG;(0YAF%ZP7Qn7_Oc%-F&6P+q3hCj_1y$Hft=V{&gUJR*8mG5t9Q_'
        'NmCJM4BuIBJTz|Mf0va?(`>1i>CTW#sq687m(+fa9!5iwXIG<yFt_<9?hg9Dyr2hQ=Ri1Ei-P1<y3V6T8$QjOULG%Mb<SRAFtxls'
        'dn1QYco9YM7cX~e!n6Yb00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
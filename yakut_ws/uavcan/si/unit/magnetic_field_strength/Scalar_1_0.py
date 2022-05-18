# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/magnetic_field_strength/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:58.261026 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.magnetic_field_strength.Scalar
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
class Scalar_1_0:
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
                 tesla: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.magnetic_field_strength.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param tesla: saturated float32 tesla
        """
        self._tesla: float

        self.tesla = tesla if tesla is not None else 0.0  # type: ignore

    @property
    def tesla(self) -> float:
        """
        saturated float32 tesla
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._tesla

    @tesla.setter
    def tesla(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._tesla = x
        else:
            raise ValueError(f'tesla: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.tesla):
            if self.tesla > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.tesla < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.tesla)
        else:
            _ser_.add_aligned_f32(self.tesla)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.magnetic_field_strength.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "tesla"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            tesla=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.magnetic_field_strength.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'tesla=%s' % self.tesla,
        ])
        return f'uavcan.si.unit.magnetic_field_strength.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8j<tkh0{?YW%}*0S6ffEWf=UQP4<6(saB%I%7MH7-UMkp#@n$BoJ41Jp+1<%}G_47V95j+lq6yFc*EcO##B?wFX5Q!T_kQ!W'
        '{<~4HO+Wu!O_*UaB8F>0rT9Wq$s>|gg{q9O9Q>nGt6gTD<{u}D!xijbz&Y&s1}SNQ{+Eu9GFnDPM6MJzD(JA}R%GN%aLI_VnwLYH'
        'N2eK;RD)k7Bd(38O2}(|<<qr&1^uOd?K@n6UnkUBEmCK>fzPmL#J@q{8@<qKKH3^#)KX%@yo=J67KN~4gb@#VvZD51bn7G)mdNSo'
        '(BHw588wy^72}X^`zM2&^pF-Eq3<}j5Jv4Ad;q_Vz-h^-X15Fdz&e2+VI2#N&os>}!Z%1u@7l&1ezy}h+ey0<9~^X&ZaYc3he@mT'
        'x*4~UPMpNu*1=)B8^=uuy<D0%d;`gn6nveqDg$4`Tk5xNF-g+NY+>h+@8+8Z5i+hc&#2`LF8yQN*O)V+Ds72iaN;+KshrL@IwU8G'
        ';{1Lk{G>>6_5tc+JP5Z}$k);<?44IZ5ciY-zjicHIhAjDQGtJ^Tq;o!nh%`}{pR~Y<jXSwVWPprdJqx#rwe2Req$!2s1-G%uvoBx'
        '?=6y3gF|AJ4VxZ`jKgKVm+vDbsl+xfZgeo;2L{@^XYdc-2>Wh&KE>m;BK&<)DeyasikL}}R)`TNIY!K=varkdifd{sJ=fJT$#Q{O'
        '&3k@hKp7L|@V}tEAG{|{BFxEMFIE^)={Wp^z5dQGlj4I?vqI2cbt%FvL>VND1|0`uCCC<u57}#kj}<MaZ|=mUCUt4_2Y0Hqy$}Qd'
        '00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

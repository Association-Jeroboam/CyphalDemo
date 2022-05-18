# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/unit/torque/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:58.607056 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.torque.Scalar
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
                 newton_meter: None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.unit.torque.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param newton_meter: saturated float32 newton_meter
        """
        self._newton_meter: float

        self.newton_meter = newton_meter if newton_meter is not None else 0.0  # type: ignore

    @property
    def newton_meter(self) -> float:
        """
        saturated float32 newton_meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._newton_meter

    @newton_meter.setter
    def newton_meter(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._newton_meter = x
        else:
            raise ValueError(f'newton_meter: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        if _np_.isfinite(self.newton_meter):
            if self.newton_meter > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.newton_meter < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.newton_meter)
        else:
            _ser_.add_aligned_f32(self.newton_meter)
        _ser_.pad_to_alignment(8)
        assert 32 <= (_ser_.current_bit_length - _base_offset_) <= 32, \
            'Bad serialization of uavcan.si.unit.torque.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "newton_meter"
        _f0_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            newton_meter=_f0_)
        _des_.pad_to_alignment(8)
        assert 32 <= (_des_.consumed_bit_length - _base_offset_) <= 32, \
            'Bad deserialization of uavcan.si.unit.torque.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'newton_meter=%s' % self.newton_meter,
        ])
        return f'uavcan.si.unit.torque.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 4

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8j<tkh0{?YWTTc`*6kg;ipoBnt(L|mEUdFxR@G53sR&XQ6H`8>cW!t1PQ+ru=O-STHBS{lYIQ~h0g{LgIh+$slwCDPL=j)fb'
        'U%zK-mtT0Q$ILR75X+6EN`9u9;t9#CLRVHg4&lMEGd_3T@ONX);R1Hg;1qVkJSk~`{wJOeb6O@=Cccy|ah3V#d2*anMGb@{GUUd}'
        'ssvFBi|?=O3+T=CYTw`t!V00z8JT&<Eqs8xCi)u$VZJN5V$(^M38Rh@7stCRT^m_QCx;kuzpE<h{spr_GU<ro<-iH(ZDGlrT1SeC'
        'aS)r~QU5wUrX>gHJB%)bQTqySA#4)sXvwHyHw%5oIt3jdE1t#1Cx+$@;ajAodu3ydu-$6cn`yJv-rH-Xoo1SL_R~h=MZMifTkW*n'
        'Y3%JcJMDHIVlSVG`LJ5@Pp&FS!5v4E=LoBE2sL!luyKP>l8q;8It8&U)-3{MTpONK#~GZ5hvY<#I3v0;jz|VaVV&5@o1CLVaiS^0'
        '2#fKjWQGv>sEScP-d-SWGtaTNsG<z+X$fKZV5|jIuXs^Gc&vS<WKIkpcoq9i*MtNtOk{(J78B>9bntQ_9tdj_`6P{`p2T&6i!5&t'
        'K`qW?c<JJPhcf4IE_TE&GLR{(`s{l9(=A}2yM2bR`ck^rm*-<VUg;prl1f9^x~qsC7g>dnaFRoWh}w!9e51LcIQUde3nUj36)L)6'
        'txp+~<>0>{(Tm<AuMp<=wihc5sX`)tz)o-Lr_Jyg=}95zE%^-L7P5>&MT3r_u^7dQJjd*1!bh5xmoM$eXEyU$@&{aHkeBrX000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

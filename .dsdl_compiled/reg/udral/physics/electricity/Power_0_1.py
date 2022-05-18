# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/electricity/Power.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:35.167916 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.electricity.Power
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.si.unit.electric_current
import uavcan.si.unit.voltage


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Power_0_1:
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
                 current: None | uavcan.si.unit.electric_current.Scalar_1_0 = None,
                 voltage: None | uavcan.si.unit.voltage.Scalar_1_0 = None) -> None:
        """
        reg.udral.physics.electricity.Power.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param current: uavcan.si.unit.electric_current.Scalar.1.0 current
        :param voltage: uavcan.si.unit.voltage.Scalar.1.0 voltage
        """
        self._current: uavcan.si.unit.electric_current.Scalar_1_0
        self._voltage: uavcan.si.unit.voltage.Scalar_1_0

        if current is None:
            self.current = uavcan.si.unit.electric_current.Scalar_1_0()
        elif isinstance(current, uavcan.si.unit.electric_current.Scalar_1_0):
            self.current = current
        else:
            raise ValueError(f'current: expected uavcan.si.unit.electric_current.Scalar_1_0 '
                             f'got {type(current).__name__}')

        if voltage is None:
            self.voltage = uavcan.si.unit.voltage.Scalar_1_0()
        elif isinstance(voltage, uavcan.si.unit.voltage.Scalar_1_0):
            self.voltage = voltage
        else:
            raise ValueError(f'voltage: expected uavcan.si.unit.voltage.Scalar_1_0 '
                             f'got {type(voltage).__name__}')

    @property
    def current(self) -> uavcan.si.unit.electric_current.Scalar_1_0:
        """
        uavcan.si.unit.electric_current.Scalar.1.0 current
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._current

    @current.setter
    def current(self, x: uavcan.si.unit.electric_current.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.electric_current.Scalar_1_0):
            self._current = x
        else:
            raise ValueError(f'current: expected uavcan.si.unit.electric_current.Scalar_1_0 got {type(x).__name__}')

    @property
    def voltage(self) -> uavcan.si.unit.voltage.Scalar_1_0:
        """
        uavcan.si.unit.voltage.Scalar.1.0 voltage
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._voltage

    @voltage.setter
    def voltage(self, x: uavcan.si.unit.voltage.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.voltage.Scalar_1_0):
            self._voltage = x
        else:
            raise ValueError(f'voltage: expected uavcan.si.unit.voltage.Scalar_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.current._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.voltage._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of reg.udral.physics.electricity.Power.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Power_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "current"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.unit.electric_current.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "voltage"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.voltage.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Power_0_1(
            current=_f0_,
            voltage=_f1_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of reg.udral.physics.electricity.Power.0.1'
        assert isinstance(self, Power_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'current=%s' % self.current,
            'voltage=%s' % self.voltage,
        ])
        return f'reg.udral.physics.electricity.Power.0.1({_o_0_})'

    _EXTENT_BYTES_ = 8

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8$FPKA0{@*=`)?aX5O&(6Zqm|+0{p;p0V#DvxyFeTobpO>m8zHoLjZw9S@!PMo)vo!ZuguR6p2cJ8fhgeW%)<>3z)t0D`}!i'
        'ShBo3vorI}%s1oTXaD)PS}8u}&2$i|P<mAHOfV^aWxnJd4U#BLl+fIo7xr|P2RhIA*MpSXW4rv=9@?6jqcMw6|4znxULIyldMON)'
        '2$aVq4|FC1p$A?k+2@%xmua78N+hv`im84(JRjS3r9JbPeQeDY$~4;ex#r3~LjUI=8^5w<Zd-5}P7p27kZDG>g9#T(A<UVjob>}1'
        'drEkDEc6&14e~7GvG(=?CRt{o3iIumcE!PgtB)+)7`j+I4@;VfNNCYVEc4qkVfti+u25fSDtX+~VA}-o1x#rgB_ZN_&Ai+hnL9JD'
        'g}NQ5az**mer3&zRB0B6EDNU{JwZPa>tQB&=mK{$7HBM{!Xj@E&*;P4T5GJVHdogg8yjoQ_0?u`eY07wzrWI`H`f}?#(I5Yb9KGZ'
        'Sg|fv?qi`Yu_)yk`kbX<5?E6~F*A!(jiLUa?E0aFJMfCa6hoe7JYbrK_Q+hLU2(uenkJd1BDA~aCRItE1soNU)0ANXrs{sA@DY3m'
        'Np{e2(qk;x%pHskiDT7;R9Lgn8l=GFeI6y&yqe~|#I7OTa_Qntx{aw{Dw~Xk3Jqsnqpi7dy4BWPFPrVvy%o>3)M{7hMG8zII`_u)'
        'xGw^3k6;DrSPNgG|D_QFCY`{C`t;qJtDg$}d2!#v>yQiPB27|j$azlGAo3GT4w39&vdAyj#V@cMOefidQI}`{0x1u>=6Z*Pp@@6W'
        'Jc2!^-OVMYIXJCF4}B(cZvVEmHhHRi9L%(IWZRc>AJdIQ?8u4-cHj<GM_8=5vtFS5AZ2keySurs{DL>tQFUFxP%@sIsUdv*)DZR)'
        'sacOdfA-*w;pwe5fwy4^Zask-y!$`sJ?ml)F)~<13TucIG>%|>7dBwC26y2D_z*sVkKq&8f_tVqL}{VrXad^>CEx*kR$zi1=!|Rr'
        '&G__vsr+G7V))Tj7AWHX3BT+REA4cZrwW3pDvpB{2)RR8gAi`QAHef7VVa9L47dl2?d#^M+`qU?r#7%P*NPpCgs)F1U*z)L#!RJh'
        'zeSRa+-ngjVopYeBy~3Amz>2KcNAA1dB9^NlazzoL<1+?M9O3zi9?3%Crb2U5+rdSFUSzW(o~}5-Gv20-Xm_*-Le}$@1nUP-7JX;'
        'f2Sg=9IXc==6XNLekM989^sM=NsW6w?>1o=0sogAy_dZ*#>4JOS0ihoCe}hLF1uwE9+vSLDYw+fwT~;0XM^Q3(-C0w67wE&NqF{o'
        'Ea*&4<4dh1b}KSIbF9sLIn@}${qddY?aOCLRB#7=<H||5P`Wjdjvk*BJED320V23OF8v1p00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

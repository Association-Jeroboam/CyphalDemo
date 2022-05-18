# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/thermodynamics/PressureTempVarTs.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:35.262256 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.thermodynamics.PressureTempVarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.si.unit.pressure
import uavcan.si.unit.temperature
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PressureTempVarTs_0_1:
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
                 timestamp:      None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 pressure:       None | uavcan.si.unit.pressure.Scalar_1_0 = None,
                 temperature:    None | uavcan.si.unit.temperature.Scalar_1_0 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.thermodynamics.PressureTempVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:      uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param pressure:       uavcan.si.unit.pressure.Scalar.1.0 pressure
        :param temperature:    uavcan.si.unit.temperature.Scalar.1.0 temperature
        :param covariance_urt: saturated float16[3] covariance_urt
        """
        self._timestamp:      uavcan.time.SynchronizedTimestamp_1_0
        self._pressure:       uavcan.si.unit.pressure.Scalar_1_0
        self._temperature:    uavcan.si.unit.temperature.Scalar_1_0
        self._covariance_urt: _NDArray_[_np_.float16]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if pressure is None:
            self.pressure = uavcan.si.unit.pressure.Scalar_1_0()
        elif isinstance(pressure, uavcan.si.unit.pressure.Scalar_1_0):
            self.pressure = pressure
        else:
            raise ValueError(f'pressure: expected uavcan.si.unit.pressure.Scalar_1_0 '
                             f'got {type(pressure).__name__}')

        if temperature is None:
            self.temperature = uavcan.si.unit.temperature.Scalar_1_0()
        elif isinstance(temperature, uavcan.si.unit.temperature.Scalar_1_0):
            self.temperature = temperature
        else:
            raise ValueError(f'temperature: expected uavcan.si.unit.temperature.Scalar_1_0 '
                             f'got {type(temperature).__name__}')

        if covariance_urt is None:
            self.covariance_urt = _np_.zeros(3, _np_.float16)
        else:
            if isinstance(covariance_urt, _np_.ndarray) and covariance_urt.dtype == _np_.float16 and covariance_urt.ndim == 1 and covariance_urt.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._covariance_urt = covariance_urt
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                covariance_urt = _np_.array(covariance_urt, _np_.float16).flatten()
                if not covariance_urt.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'covariance_urt: invalid array length: not {covariance_urt.size} == 3')
                self._covariance_urt = covariance_urt
            assert isinstance(self._covariance_urt, _np_.ndarray)
            assert self._covariance_urt.dtype == _np_.float16  # type: ignore
            assert self._covariance_urt.ndim == 1
            assert len(self._covariance_urt) == 3

    @property
    def timestamp(self) -> uavcan.time.SynchronizedTimestamp_1_0:
        """
        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, x: uavcan.time.SynchronizedTimestamp_1_0) -> None:
        if isinstance(x, uavcan.time.SynchronizedTimestamp_1_0):
            self._timestamp = x
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 got {type(x).__name__}')

    @property
    def pressure(self) -> uavcan.si.unit.pressure.Scalar_1_0:
        """
        uavcan.si.unit.pressure.Scalar.1.0 pressure
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._pressure

    @pressure.setter
    def pressure(self, x: uavcan.si.unit.pressure.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.pressure.Scalar_1_0):
            self._pressure = x
        else:
            raise ValueError(f'pressure: expected uavcan.si.unit.pressure.Scalar_1_0 got {type(x).__name__}')

    @property
    def temperature(self) -> uavcan.si.unit.temperature.Scalar_1_0:
        """
        uavcan.si.unit.temperature.Scalar.1.0 temperature
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._temperature

    @temperature.setter
    def temperature(self, x: uavcan.si.unit.temperature.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.temperature.Scalar_1_0):
            self._temperature = x
        else:
            raise ValueError(f'temperature: expected uavcan.si.unit.temperature.Scalar_1_0 got {type(x).__name__}')

    @property
    def covariance_urt(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[3] covariance_urt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._covariance_urt

    @covariance_urt.setter
    def covariance_urt(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._covariance_urt = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'covariance_urt: invalid array length: not {x.size} == 3')
            self._covariance_urt = x
        assert isinstance(self._covariance_urt, _np_.ndarray)
        assert self._covariance_urt.dtype == _np_.float16  # type: ignore
        assert self._covariance_urt.ndim == 1
        assert len(self._covariance_urt) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.pressure._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.temperature._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.covariance_urt) == 3, 'self.covariance_urt: saturated float16[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.covariance_urt)
        _ser_.pad_to_alignment(8)
        assert 168 <= (_ser_.current_bit_length - _base_offset_) <= 168, \
            'Bad serialization of reg.udral.physics.thermodynamics.PressureTempVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PressureTempVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "pressure"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.pressure.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "temperature"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.si.unit.temperature.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "covariance_urt"
        _f3_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 3)
        assert len(_f3_) == 3, 'saturated float16[3]'
        self = PressureTempVarTs_0_1(
            timestamp=_f0_,
            pressure=_f1_,
            temperature=_f2_,
            covariance_urt=_f3_)
        _des_.pad_to_alignment(8)
        assert 168 <= (_des_.consumed_bit_length - _base_offset_) <= 168, \
            'Bad deserialization of reg.udral.physics.thermodynamics.PressureTempVarTs.0.1'
        assert isinstance(self, PressureTempVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'pressure=%s' % self.pressure,
            'temperature=%s' % self.temperature,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.thermodynamics.PressureTempVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 21

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8$FPKA0{^vG-ESR76~EVszZ2)fNtz~UIw>WwOYYXb_H}Lw1%iW>u#FSNNwJ`0HM={$GxpxyWoFm*tyGCVfD&n?u9QXUKLE;~'
        '(1-p3m5PAJNJu;&5EbGT)F;F_yR-Mhb^sxW6#r)D<9wepXYNl9|NPUFmHc1wYS?j=>lv0}QczF4Pi>DGmJ_tYK#7QD$<eh)#!eJV'
        '_Mj88>}fXpVfH~blMGuvZNqw9vX&9Ml6pqSJ4!gph&Yq&!0o^W{JbZbQh1)V!*{8Cpt5Al+GbLTz|VLk8GToepJryoto|(fFiR#a'
        '8bwmral};iBVhLeLA$%MWOzj|&+Q2~VYxJ-R)kXXp<<E`CzoQn?NHx{M4K6F9pB+H@WuPgeE<_GqU|u_qkP<~niZ6U9|7+CxIRAp'
        'A~`}S+9DF$AjkAWUx}8_+}nP{T1*a_ZPKzuWO>YQMLaW`Af-c9WP!Or$_vSvdnF+}W-P<n9b5v_RDYV?&yrIX$mqLNy8VQn#5Sll'
        '3Fel8Vou<@S#sEN11DSm%TT5AfHUI9ZJS9FY>>WPibR}7gwt(CLaG#Vi4wlUhzi<_Pzfv~l^xQCPd_5UhyD4^$e2K)dLD=dQnX-s'
        'Mi|Vvn(smb6PqeFON1gW+Yn$A5;9q%Vdx2mM&NUUAQ>l?66ti0Ag5Td32+p#8IkPAG57|KZ^)qCqprH{%ZZUT2*%`9q8Q6JIRVgB'
        'At);R7R<_R0lMX)h@ATbXaT})Q!i#HWfTyfZKIjs&xRN56!LY~8%s4X3E2@Y$jKZEGQKr2K}e0%A2pT+EeqSJ9mEl-*P9K}VN|NC'
        'WQPlf<5CEoi#i6mL6#PCntf+M?igZ6lAR#-Twnwo2#I~4Igm+I3a?X$0D(Y6q`K0A+29yRiymnJ*N6wP!d*FgSaxF|K`3wo!faQ7'
        'z5EE`m^e}>p^QSAWe;LOIJM;)t7OIxBC>LGmOv!<U`q-794a9w;t=h1jo2MXQsfxYju+6}$KWWa4n{8cgVI%`jpDapv*OhA(8CyR'
        'Esxdm?FEYs)-zO_!9)?GQP&R;6jve)3$%g6RUaHfz=+DoAQ7gLvE{(WG>N)-$EW#4J-TEz`D^@jvx51=uN0{>`f$};z5D&ujL#;Q'
        'f52q0mvtU*;5W3!mLKf+MwX0Nxj<R+N?8=xZivMWL#w|ejNQ-UlX|5*ypfE9$_~zAIb6|WSWl{R8A_(?*k;LeUmdjUPEm7Fiy3~7'
        'FYsCn1;u5+6w-;g*^^|-+7P?Uwa`(PaI@9qgr$O5It&&(W`z{WMKX%u2|G*1??Ij4y@#_;p*&UJgu=lCEbK#}$dZZWP6)ob$=X4d'
        'oDX9g64!!?AA88JS7AYkk)p7|d9+oQTs*M28uP}SfyT-rEN9aerwW9^^tW_^W>3HgpRX1Pj~obcz-WQ|4<u9rG&065BsGPEjdlXL'
        'Rm(F%_3_MomNSJ&iTFT<0fE4aiyDxZfF2+C;G)GL$H1yV8w#AO8DqTK0Z@YKR94|U2e)BQAZsdQj@S@=aSj*67BjFG+a8$cav3MR'
        '(hW*Sd%v^f$ah5aPX4{dx<Q;AvVt&6$cu=mPTLN^KVa26;4fVi??N`xD3HA?XvA_jq<_ZWOOD;6F4o3<n>fYQ)!6f({O?`mjgPV!'
        'vzaOzF7mLTkeOq#4SKePkJlOu=q?UM@oIx;L84|A&s9=$NaG>Iq0~IAzlRa4sX3zONA>)e#&JDAfjE+ylY0LV#Ie*oig-9Rr}X|~'
        'h?A*#T(6%%98S%Xn$9%h$<#cBcsw;vBTl8}8N?&0`4ZwpYM#~SU)FrjX+GyQoeP@ZD~RV)^CIH8)O;23<<umIXH)YM;!COd8seGM'
        '{0idf)O;QBRBC<|aXK|GYq_o<o=D9ZE#EBSvDAD+%lS3Lqp5jS%Ujd>8d~l*5yw+=PRl=!IGUPut;d44$D-CJ_v@k5T+(`7)Ans@'
        '{jL{&H{a6ub&cQ9__oGxYW$YQZ)?1zaa|+VxU2E8#*Z~V)A)(T&on;Q_=UzV3%oN{)q}I;V5S^2%fYR3uwD*$IoK@+kITWw<=|O4'
        '_@o?sRt}z*gD=X#mwFIGcLz5D+#^`p^_-1`9d4ZQsMl}KCKbH6x?N^pyLwT#t4bI#G%ZG`n`vXsp^%&VdeuH67n1Q6xR0ZO1{AJ8'
        '0@q)iUwI7DwP_28#@Ktlom^R1oU1qM3yVuj3(ZEo*=$^I&d*<)Tbyq$EH)P#^Gnz3jm5>{ddhVefld&_00sDOVw>_CP#gZhpDVun'
        'gx_4{-{rSv_-+0@Zt{2d9ln|jDY#M&qaJYQm6~M9u|k)@tAVdQL9+ZIUoVQz5BZ~RZF0J!R$oOTP?7i+79#F}mTma&e~^{cL-Aj&'
        'cCFvzUdVo+?Jw=IeFP5}tc3rW`G2?1;QaUhot3wkw+&^r&&r#_)k=l`<3)z%f8>8kCi}$A_@Dp(HXUTR$E?si9Q=Tjl6K%(vw~eq'
        'apm2>sliv%QHyyDpBnl(*R$>Me%lT&H5zk^+H%P_Jgq|Nh^Uj9hYr^Hz2xM57P3ejd{YitTX=NPBFEEQU(cKaYs}@=s2*UADJR&5'
        'R-M9Y%8F%#N&X9bOT-~Qf#9{op|QkuXn(PJF5WBU5qQeL;x3ul2s~))vD3i~dKR?W!YLVhtoO8nu4GMjAo<Ndi|zLusntl4rjP3I'
        'J>UC&qlhb*tm9<y^{5V}V;EyI{MY;h{~Q19=4lMJzi-w7HqXGH_`tAB4nbcC&+z=W0BkXfUjwpaYVh}fEIGID7Xe88`8}zh{Ic6K'
        'V*BOA0v;CnT;6o`MH`t>u+78QtM32c+2eI)i@vXCRb%3=jZG#i`+8A4)1aFxe&c|Lkc#cR4Fs3;(!U_TxA^7-EBklZ)E{l9;bDTE'
        'x_@A6h7pUM88pNAo5#PVwz&eH$Uio3!{~pt-|8lN6T-WR;hje{|0`2CyAHGKz1ec};PmDZ;85(}g@xVz{ndE?^ycO6{%5f8Y(M?M'
        'X-qNWpQAD<y~h#&00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

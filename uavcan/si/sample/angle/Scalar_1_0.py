# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/angle/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:08.189035 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.angle.Scalar
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 radian:    None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.angle.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param radian:    saturated float32 radian
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._radian:    float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.radian = radian if radian is not None else 0.0  # type: ignore

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
    def radian(self) -> float:
        """
        saturated float32 radian
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._radian

    @radian.setter
    def radian(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._radian = x
        else:
            raise ValueError(f'radian: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.radian):
            if self.radian > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.radian < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.radian)
        else:
            _ser_.add_aligned_f32(self.radian)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.angle.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "radian"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            radian=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.angle.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'radian=%s' % self.radian,
        ])
        return f'uavcan.si.sample.angle.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e1>&m0{?Ya>uwyk6_#Y{w(>Qy9mh@_I!!I9^-iRfR$iw~Q&+Cxl<~%h?N;c;1I`S!Bs8~@97!9XK=Y%81q{#uJO%Oyd4xPd'
        'fEI0k27Q8{PmrHIXNI#YIko`lJHyL4hv)K<`t!-ZFP@&Le)6}|VW5N1aWz+xh4M4zh1_xdBuW!44KMT4kBrKElPUgqnDX*@x$=4W'
        'r*b);c4HR7{975@^I7a@>1Y<Eu$#pL`1{CbAyZ{O=k9T(WfGTSBA@-Wm7kY%l1}`!{JhK;TxN`tUS_y1{{Wg_;nQeUnNQ!7JPgLZ'
        'wA_Fh<{ETROx1&8I=^mRGcp2yhOsYH63fqc@E8WP0dGq&E9M(d#3`^Y&e`pYuks^RGLlB_fgg)cVl4+T4?c<wA8>U%LJO`ZjT`cK'
        'U_?oK;HA&Baib&vFW<~BJ!}-=HfIaw9^e#)<}c-^Wq!d0ALD?j;HaX*%!8vXMABD@=6(_fWq#5P62IL3-_*p!W5G$BMIKiq*&#<('
        'X<`I3M6f+hQl>Qzh?cR>iB2L;m;w`usUeBrGd4uVu)bPpoE9pz<DfKAasboI(&5g{Y83{UcueyZA~gy4j)a(yl&dyN(@^@%K+YY4'
        'YWz$o)HB+GmNLy-kSOADqWB*($PH}YQAsq`u1D#sl#vJ=<LV~SoL7td1oY|@4l3gTjH*2eXRBP1mGu^!0-W1pVaCx*laQG2VVL00'
        'PMGZ1{*C6ln{5aQ*_Q$M$$bVszTavQ(k7j!-Ob~Xh2_jkGDA9@UY86xQ~D;^7t$9v1w9d)p+oMF&5cUuk-gw|2DPKeev*X&7y=7~'
        'WO2-Wt~FCK9M&#CArNWw$Xf^-Yy)pGBVDj+M3QM-RhftBAOjVIfi+Of4<y7ZHc-dJS5iyu)Q8y$p%$dy-n!E#%W-1Jy}K&}Dj|kg'
        'DzN7>1x1mi7_VEz8$y$!#gq-hgjG3)L;(>vmE(__RFMeXAHZTQSQui4vD|<d+ST&f#10<^D&jCu*Qgog0g7VDU|C=c6wbzw7y?1m'
        'P6>^0CZF3%Vr&yL>N~M0u370i?TL59yL1BkNi5Z^Gy9}Z`=9)#Uy7Cd#&5YwUNl|R8{`e6u^T7*u~X(VZsicrT|)}|AccZMGCM{I'
        'bDviA$->4T(aq=K$Ucs0n7?Obn9nCyOY}^8naA_RBRuGO!<t_46wBg@SQqUK2qoZP6xxXg<zart-H``8a4}J?49b3f-qlH_d=3*K'
        'cT)y*k<TK8(kt`%hd}8E4{`K4(9`65KpY}L4xdV8nYXrvDdg%dkCHOKnr0p}uB-SU3(?+~Vc`%nHL=2ej8&Omdnvg(YtE{J!72^X'
        '*`h0$2B)z7UE84LAtd1+{kq}N0znH{Eztjo0ye-PW8FeiGiX?|pQzn-)e-uL%_?V=QK%Fnj&&F)NW!e<fQkafcHl$Efq))^s3s8*'
        'Two1jy?O~~0(NRxxaz?@Sd*x>PPs34<dHgu3u2c$$i-d=A-d7j$(Xv~(B{SOGC%bTX+EyLAMsHU=O^4GEpzfJC3+Zn3FHT&`T+7}'
        'N%0ftMrIN<zJg|4UqJhp;`jO4hb%yD{N5tLaJHX?a9s~yoE6=_mCLkOXb&#(wAN74xy*xeMl!~04Fq<8!Yp2GP%WsGPU60af=*dH'
        'fjCvrllFTWak8K@c6`>3&sm(e<1NIQf-czgrx51~dK&R$LC@IrXAu_)dd|+DN1QI`YgW%9;%f!HfOxK;7ZJ}C^b+E!g1(N}D(Gdq'
        '{|#&RinVjq>Uq=JdkgVuL9ZcRDd^jXZxoauUM}c$#McY@4&tSP{s8e}LElBZP|zPDE*A8L^=k?7d_kA3e=CS*3;HAL=Z_Ij7xbp}'
        'w{6esSij#xoG<9A^?wa<wxAt*j&&Q44SSv{uO|w+Y0q`b#<yqBce~Czec$3wEdJEu2Nr*3@k5J0w|L*;wnbs_z~VEDUs(Lo;#U^G'
        'w)l<3Z!LaT<Ab?LD_m}b<woc=!u>|rZUoT?2aWKo5x!`IFB{>jM)<lBzG;MS8{s=EWbnF!8v*VSq;@;zA+f`aGjGQ4&6RutFRsxm'
        '6CQ%|_uwiu$KH-`a}l_?I%4S=D2~_w9x)j{8$ZaG);Cr=z0Uf^=H_~@+v)YXw|i@Aw^ldSdg~j#jqcj!?M`=NqrO=x^D~MC64+X-'
        'h=0RHBkrJqe~I(rzv4fc*g6z<`{I}4{<8Q;{7O*qv3MZ*`ILq$VWxi3!-Kne)0g?#`c;3N*~OznR4tx}?V2-wC!UU|#UDvekI>CU'
        'xV7;bi(krH`Fu@Va8uwv1TWR*id{Mh#|z<#kKi{3yZ`LNz~BgP5#TMZanUv`+8!_3MGE`gFs94-KYkG$;2sSC00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

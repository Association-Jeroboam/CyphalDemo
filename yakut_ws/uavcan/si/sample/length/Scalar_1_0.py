# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/length/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:57.801202 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.length.Scalar
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
                 meter:     None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.length.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter:     saturated float32 meter
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._meter:     float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.meter = meter if meter is not None else 0.0  # type: ignore

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
    def meter(self) -> float:
        """
        saturated float32 meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._meter = x
        else:
            raise ValueError(f'meter: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.meter):
            if self.meter > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.meter < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.meter)
        else:
            _ser_.add_aligned_f32(self.meter)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.length.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.length.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter=%s' % self.meter,
        ])
        return f'uavcan.si.sample.length.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8jkSbg0{?Ya>uwyk6_#Y{?rUT_j-5Dkl3G&hok*))d7U;*9l3@R#v3EDTcH;ZI5X6e(A-LLByE5K&5srqFhB?J6v!jw5%LHD'
        'QndXU^a+AKL4Nj}8O};_Yy<XpmgJmscrM?e|8nvl7fz2=fATleVW5N1aWz+xh4OReh1_xdBuW!44KMT4n?_~6$rOJyOnLdNT>hf`'
        'bGejHx-pAj|60a&eHJ@fI+{f(d>!(5V1%>jvyiDWpK*7&(lUulF_usN#>&r1I!?#_R(?_D^DZ++NiQ>8mwyD+FL7#gs>~<vNgf7='
        '&dj+1Gt4#Up_r%_#bkcn`etOroy}qF3zfw3a~?c`1#Q6HQcR24#uIT0tc!E@^M#lBkt!KUBX_}%g~zd$gO~>&#fA^KIv%2V*OSJr'
        '!%@;6c<D23+$aga%h&Tu4;w}JnX>_V4{!@Z^VjmTGQZ%0k8!|Ma8%Jj=E2qGBk8L|b3ciLGC%1CiC=F0Z(?lhk>DiGB9AMQY?C9W'
        'G%<o1BG@h`Dbtz<M9bLcL?;m^Oo0i-)R08*Gd4uVaK1WeoH<l#*FkBb<N&spq{E$?)hP@x@tEezL~0W7Z3!_UDOW9)rlItift))8'
        ')%clGsAu#ETFNw^gG3RJ6UG0OL2lslZIwia+Vv=Xl`;~6V_e-Nn)B+ApMYMS!bN2~fK|0C;ck^Hva&u0w*cpMS(tJ3(j+A2yBH?;'
        'XFE*xYX3(2-SrlPgzU)x{Nz3ZAK#msBcw&zPrB>JBMZlwmt=;t+r2Isa;Ef6vL~c3a0{9uHbaNpA?uw==aFy0?+j{3k-a1f126;@'
        '2+87@`&?_LWH_u{fI=YB=#jS&Huwy@#f)^psu4-1@l<6Vwu1~*5C+yjG2fREuh>8x6JJR!wNqbaBZOLzerw}SpDe|RA@}Ys6R3n3'
        'VyVEM&lD6zmSVha5pM`hiWXBg3=>x67!n0c;8c!3YEnfabbkPcwP0b08OCxOguGQ9uT5<8!$3tG7U~)`qdY)SEE+5ejDf=47!pGu'
        'h}tQk5zgc@8%d09Vn%%@7Q{6xU8g<qmUxGbVLyq*x^<=>_i6vr-}XzfoZt8zSIP6Ht9paHVKjE)WG{Bge9EmHD)ToQQsDb36daP-'
        'F-n;Etg25IHvWiiJ_}d&aaF_qJuAb0KE6_-XWGj=o-Z8XLDw7B{ED|&5?92UXk|bs0SBYdPCO_N@-yzX+~<LdiE?F7_Ve?uPBP_l'
        '*a*3sGN6lm8X=Tkna@51PTzlstIvR*#@_|v5DAj_L@LXCZey52uI}<EDf6po=0W4SiVw07?Hw{KTw<ywR`?!c1w-J4<m#+CD-H&$'
        'G)QL)u3#FR!uEG<gO&%7gm3$G!=nX)7O+~N{}TmlfI-H(g{EfEux2k&JFTiC^bwm?&MKo&DMlRYFi?<$S<L|z1svLeA3_cU^cX}n'
        'iGbh&YZ&X*OF$E_Q^Uel5AMR5M74CveYq`<)Hw`@9qu3(dm)7AMpGw;)D4$5&;Ks-Qy)t6N%eb^kBT@y;U;OBlb0#c!^le@KM>Ui'
        'kS|M$pF%e>lc>WHH0AmN+P@Tk$j?4x0dnJy4he?4{VarWJ$!ywbpKv1(O#iF802ZKp`<gJ2ltF*jAIQ1wvWOzjy9+kR7%J3yRm{!'
        'SUiC^QP7k2_ax$YL8t8cv|XREIBVDE5T^<{Z_l4XoGIvO#FGU*W6z&OoG<7(yMG>WvY@Y6Jqw7h6!Ze(xq@CqJX6q1h^GqrD&ky0'
        'FWc{5vv#joJ6Elq*R8!b5U&>W8se3LzKQr+K?&mJf?h{_wV-byUMlF@h!+d`4&sG^{seKMpf{{vi-_k7x@7%ZMm$^4pISeEhIqQ5'
        'H?6-ddtb-;{Vw8cL07E*tBBJDZQFaS*?4s9eX6{kDCoMq*DV|0p1t4gI`8y7i$Ayc3ybet{H4VYEdI*keT!Qbg~fe~Pc43F@hgj8'
        'Tl~i2cNV|5_(P2kX2z{>xe=Bcq1Ooa8)2&vL?i4s!qZ0hvJt*&gs&Unn@0Gq5x#GPAFPnU>kcLY%n_t^yXGOW!^D|2hwshhd<+NI'
        '=#>c%!P$E-O3ksiBTOy=ldCNjpMv6u4d4-z;j{7md~vO_((bj_I_v9ey>7eL>)!6IuHIVdtoGJAy-s&^{dT+C>C}^@GCvt{cq)Kt'
        '@o$(j;tuNnmpCu}EB=#-jRSGFFMciVFNu%D$AXGa!~@aKCp1iisrp3^f_;1DXX{t}ab_2r2dG;-7F#uE{9Zg6QHwv4o*bc@i!ilu'
        'jKweHt$enoEtnMeAA%QZbHxrFhwFtf;v@JQgWZ4jVPSBDw+QeS*LY|P4s9JC+Cd8Y(K4pX`9Dg5gC-vh000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

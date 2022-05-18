# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/electric_current/Scalar.1.0.dsdl
#
# Generated at:  2022-05-18 08:39:26.803180 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.electric_current.Scalar
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
                 ampere:    None | int | float | _np_.float32 = None) -> None:
        """
        uavcan.si.sample.electric_current.Scalar.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param ampere:    saturated float32 ampere
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._ampere:    float

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        self.ampere = ampere if ampere is not None else 0.0  # type: ignore

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
    def ampere(self) -> float:
        """
        saturated float32 ampere
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._ampere

    @ampere.setter
    def ampere(self, x: int | float | _np_.float32) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -340282346638528859811704183484516925440.0 <= x <= 340282346638528859811704183484516925440.0
        if in_range or not _np_.isfinite(x):
            self._ampere = x
        else:
            raise ValueError(f'ampere: value {x} is not in [-340282346638528859811704183484516925440, 340282346638528859811704183484516925440]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.ampere):
            if self.ampere > 340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(340282346638528859811704183484516925440.0)
            elif self.ampere < -340282346638528859811704183484516925440.0:
                _ser_.add_aligned_f32(-340282346638528859811704183484516925440.0)
            else:
                _ser_.add_aligned_f32(self.ampere)
        else:
            _ser_.add_aligned_f32(self.ampere)
        _ser_.pad_to_alignment(8)
        assert 88 <= (_ser_.current_bit_length - _base_offset_) <= 88, \
            'Bad serialization of uavcan.si.sample.electric_current.Scalar.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Scalar_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "ampere"
        _f1_ = _des_.fetch_aligned_f32()
        self = Scalar_1_0(
            timestamp=_f0_,
            ampere=_f1_)
        _des_.pad_to_alignment(8)
        assert 88 <= (_des_.consumed_bit_length - _base_offset_) <= 88, \
            'Bad deserialization of uavcan.si.sample.electric_current.Scalar.1.0'
        assert isinstance(self, Scalar_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'ampere=%s' % self.ampere,
        ])
        return f'uavcan.si.sample.electric_current.Scalar.1.0({_o_0_})'

    _EXTENT_BYTES_ = 11

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8zOaO10{?Ya>uwyk6_#Y{?rUT_j-5Dkl3G%0O>|p%oi<G!xrP(Q8zZt?p%)K0Gt`pM+)8pJZGZyJj}{g%KnE}j<Pq`+d4vEd'
        '+Wrjs1VNu5KYPwBXIFA;0n&Gdmvau!<s<c%lmA#eJyQRaZ|1#7N3rK?t|W`)=PZc1=Z9I6XIdI=%hOv%6`?5<f7HvleP$QGuz$7-'
        '<+z`+1m+hCwimM0)6&x{$zeB-d1#aj{jgAqr^ed~S<I9zr~Eyxw9HZ~M#{<GIQf~SqjcnN_6u9i`pm%2pfFt9KZ22$xHnj3%kg`X'
        '$I;NO89!o%`38LzWBoxfUS4-z8kul!tCxmCWvTp}M~`4Y8*to;Nip4cB2IyIan5a@dzl}(l8H2O5B!*WoNC!kdGt|gc$cf=!J730'
        'Y5bU{T_Y@QgO?%G#!s>cynMa9^srHc+q_Mfdw^3In!no5Y<a;4AJd4b=%}K@B7mdKCNfl+=3$mbwmj)aS!lQaH#RczNN|!CNx&7!'
        'cF2)cni#<h5p0i>oN3J?qGcL#qO*h(roe<^sz(y|ObwAKtglxZZw8gRaZs8m*@fu^>2dF7y$S<N0;c&Qk(xw&M?y?U&eamj^H_$='
        'K+ZjaYFv2?x1gm$^BG7K2{=*wPX*)#w(qDc8EV&q^wr8p0*-NYlW5NCMPUYdbq)uWX%|M-o`kd2uE^T@44eX-+hcLT(Myw&l<#4f'
        ';LlE+?f3l~%(pg{AS7g8M&Kt88Tk0#%nTt*Wc5jF<9K9YISaDFkk!?8i}W~C`X<>IG88xk?U9<ENA8e~^;+kVz2J8NwWG*>R>Tn)'
        '0t<u`Y05*cHB&O~^<98MAkyf8w-7ei2Hs*uT42?PtkAfsHV@NL0V)UsYoM4PNQhTzppHqXq?X$2A7(R#T9Dz==A8~%NHat3-CZP5'
        '2`R)<fxVC^D2gJ-c-<mF51JG$=ByWItj;kc3OK>59e>oMiX`ZM7Zz*5;utfG<<^b)QoX!yVuud{m2ep7*Qgof0g7VYU|C=c6waoQ'
        '7y?1mo`ps@Q%-GWDYl6j^qrU!*PL{nw#8fG9Xf*jB<B0AGx@kfJD>ixW5r^5<9A$T&zr964f2N3*iEzj)U)M;Upr*WHyTpl2RRfR'
        'lG!mznEI@)PZl@+h*mibM-FjR!~8ub!+bfqY|%3v6ag>ij_{x#^!iMTr&thI#F|(tfKVb1MxmW}WDm<T{*FB0k&lV;Wn??$d0%IR'
        '3OP)~+|L=%MLCHO%fOb?4}ske9^&XTpr_GyfjC5lbUv0#Th46ua>&(Po@BPXnil~yuCI8vh|%7VVc`%HePV_E7%N*|dm*`cE8en)'
        '!LkPFY|a-<gHzc4zH3l>2ub+1({FgRK+pnK3-o`cfDJInShvvB3>wz#XKHt;?g)LvW}UOzC{&6O$2trYWO32wfSLk^cHl$Eu7Dnc'
        'sAdTeT;vR6y#^U*0(NRxxbDF{Sd*zGo%2xc$Rl+Q7sM|2kc)#DLUg04lOc7(q0RH(wmkKrG@sPpTYON&<q1E_ZAo6HME8;)gZw~L'
        'A3(kwDSisw$V{e&SI~qX3TS^T{!pHM$Rgy%A1x9LXFEj<*LCmtS<(8tU7+ns2XK++eGQgQ6#<+xkttqlAg}`zCh=;6YC)xR6!(o('
        'bj;xi#IcH=bl>BMqZOTS<CAWD%HgydpFy0c=&W0R3UR8Urx8z9^o(177IC(s=iK~x#PN#0;`GcRzEaT(i03ML5%Ek#FCm_)=&Oh`'
        '6}{~Czvk>-adxgcJ+C`^Zy;W+=rzPE6@3%&wTcqN%N4zj_-aMpLcCPbw-GN^^c}<t75xd~Tt#m<zvdCoS9HPow}^PQqCa(h{tWSS'
        'MQ=KPm)v<h=l8pa(-mEI{;wcTR&>>!W6i~5-JPe->xqhPxO3fd@ol^F-R|d|zUT1g4u9eBeTTnv_<_S;IlS+1+o5oH;P9!#FCBj6'
        '@N0+PIQ-7x_YQyP<AbSDCtPlXg+^#M!u>|rZUoT?2aWKw5x#7MuNvX&M);-?zH5Z<8{r2h6!5x(8v*VSq;@wJAhE-ZGi`?N&BbyA'
        'FRsBW6CQ%o_uwiu$KH-`a}l_?R>k~NP@J$XJYoubHojlZudOeywpZ8IH#XMVt<`qBb-TT?a%*{grM<S^UT>{z++J<1ulH}3+WZ6<'
        '<_b11ihsjJBkrJqe~I(rzv4fI*gO<>JL1>k{(|^Od@QK=L_83ka!kXOFwuY9+w$D=&wE>*?LY93lf2kEL@VO4*zVKE@5Pe=%Y*~z'
        '$r0wc2p2fsXz2?nteoyM7}&)B4PL0t7rS&6P8!2)pTKVlcK_Ldf$k9sBS2wX<DzX?v^`w3i){9zVa%NOf4J2?moyCk00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

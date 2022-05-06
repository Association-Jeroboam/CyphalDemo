# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/sample/electric_current/Scalar.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.476611 UTC
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


def _restore_constant(encoded_string: str) -> object:
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

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?Ya>uwyk6_#Y{?rUT_j-5Dknp#rpo#?jmI&Ipzat)`9*G8<QYSDDcnW2`1=dvX^k~Tnr=0^()7$5_f1@Z`aggiok'
        'qG<asKwlu}6Xa*lnc?h8jx9j?&hT>1;kkUI{&Mo~?bBn`Pw{4d5a}rPe9e_)vHX+;G57p1OZu6XhTG!wW25rW<ce<(`rJOV%b(dl'
        '+ofXCPgw%<OF7#MS?X!&X_oY1H;;K}lnnhaSBj^`dmOTuDO=3=dt7OmrB;j;(;qwenWf`&>~HonTg>~+z|J5yT-#5;$V=QCuCm4C'
        'J;~!}<kp-YF~fX=zKV%@P)rurotH)?+<QDoL!q)%e#)b57|;eBw_;k%HlB!6U|pPZ+ZSHuM_<WA8o394EPRw|*-Lr!erkA+tK-3%'
        '_XBDCn5R7>EbV}oA=AcBvIx9<y}0zKQH0yPEtq?NQy7}R+7E4U!3Q7Hh^gqPqQg9Zqs=EWRGH>smPWQX=|@>;cm6jqHnuG|N%JJ&'
        'ie$Uw$SO^YV1@{`$4Q@Q%_E{^8ginugcGK~gkowy68KCFktwXNRvK>(mAY|Inkm_X=_ToL?`E|M155&@`7)83M0{65Oh})r7VGz8'
        '88QPo_Xw(S<uTfVmU7MKAW<aXMDai6kQ>;(tFmOIT@TY&DI*Cu#??)tIj<Il8R*r0IH*i}Fsk+>oUL+2R@Ud>6yV$*i*t@%nvA4;'
        '55ok1cH?Zn_HQ`f-fTfg$i9rgPaZPx@!h#OLRw_)5ADt4k%i?f$Z|v0);eu6;7sY8WM9Zo;1sk+Y6c#;LpC=mok#Y9-#OHdBKuh$'
        'M_>pn5R#`U54qM%$#_t^0EIxL(L-+`Y_JWy#f-GUsu5YPaaCm=rlTBG5C+yjF+Y$Huhc*tlTb-5wO1czD~4K-VQcG7mn@~3A@}Ys'
        '6R3m~VyVDh$P^Ss-p6>|BEbNf6fO4IAkJ8oV@MQmf>$}d-K2^n=zb3tYr*0eGmPcdi+QVBUYpqEqd+Ab2I?9$!#qGyEE+5ejDf=0'
        '6cR%qh}yHz2xp3!tt`bhF~hzS3*wrSuG5ZqOT10Tu%E<Y-8$1Bb!qqEZ@N}27dL*#Rrb8;s@@=P7>y@swx4>onDQ%!Z1F}z3jClC'
        '1&3sIj1p!(tm>1+jX$DY%)*gF9Mv#?&&e=fjIUVqOb2<ui-jXR=m&$EY4H?G;)+-otsDp?;$RfoiAVOZIOFfi10MO9C|^dlTb%cG'
        'maCA%M9lp@1G*@t5n>tGV)hZR`@tg|eFpS2{tgg_$dJybpm?C6Y;mF|jV<Q327SodU7lpNxZ2MHXklORULK?65!b?oshVOz6GqJz'
        '*Ir1o-m16aVc4ueVq5S9)8HNwf$v(?9zr_)(XCq_EfBPTbpuS0Dc}VRH&!sTH-pwS`<Z&us(M2ou~}uWG72?g#Iarj1zDWeY*3NG'
        '$PRo6*%Q!h5Z^2Ts*9XqtlS_2O~6wPA6MPD2Wv9b(tRGvU3sM9;i`DTJ!It|h7jFoDrQ9DaA@=Vw=GWnQkoB{@5g*t&cz8o>)V37'
        'Oo<*OK?eDOs6K#vIeL5ueaTFwMwii)9||A>D?TaCK4KBF<o6bd0B5^-3>Wv{`B~Ba+%C~hsROvu`?Us3XYv5fnaC6`I1tzY3e$MW'
        'LA9V#I*$9sN;={21mZ+VPrC0(#PO0&x$$W?KI3rKjn5%Ym2}>%KZQ6`($k11OM1qwKZ`hD(sOS9JmO?YUvYXC5ML?j1;leDy@+_G'
        'q?Zs+mGo7_xsqOX`(JZ*uQ)qbou1d7y*CiAmh>9pm6E=R_*zK`;^mTFM|`!UZy{bP=?@Sumh^4J3nl#_;zCJpIKLJV&zE$``L~RC'
        'wxmCDe*PHobV+YIe_QUnp7Z-1#MzRrIR94>r%Sr#&av*|vEj~B<@H2KH{H2zx%hV6`EJ*Fr|&xaiNl{de9z&}9RA$lFC5-?xZ_Yb'
        'JaG8b;TI0SboiCSuN{8l@LPx9)%aj$+zFQ(VW|;1jc~sab{au6!a*ZEZG<lx;mbz&su8|!gl`(*+eY}#2|2v;;BJ5$1xenG1xWF5'
        '_sp8n%X7IH!z*m~-h?ON>^-<t&9PS`++hUnur;yx6ci_{2hW)tACT`Ai|ZRJYn`?Ajm^#VPJ6A>Y2WUwuHIVNSnaHDbT-<no4426'
        '8yoc<Q<<Lv!(74UW$|yga>N}p@Go&*{8#)Z7h8woZdd$D++Py!i(d;WJ`fK?S3E2xv;?NFANsa9_xw}e7H8|n{&AWY+lOdJd@O!j'
        '6Ugs{KjfKcDEUXY=OSF@c)O)9B(Y+)<}k2{|0ldq+aE<t$Kk9A-25s0W?=W9T^JBYNQ?l9agB?1VA0NKQH*@{y<yCq_kV5Ln=L>M'
        '000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
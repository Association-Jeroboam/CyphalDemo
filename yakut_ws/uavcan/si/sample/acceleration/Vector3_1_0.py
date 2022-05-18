# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/acceleration/Vector3.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:58.213745 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.acceleration.Vector3
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
class Vector3_1_0:
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
                 timestamp:                   None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 meter_per_second_per_second: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.acceleration.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:                   uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter_per_second_per_second: saturated float32[3] meter_per_second_per_second
        """
        self._timestamp:                   uavcan.time.SynchronizedTimestamp_1_0
        self._meter_per_second_per_second: _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if meter_per_second_per_second is None:
            self.meter_per_second_per_second = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter_per_second_per_second, _np_.ndarray) and meter_per_second_per_second.dtype == _np_.float32 and meter_per_second_per_second.ndim == 1 and meter_per_second_per_second.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter_per_second_per_second = meter_per_second_per_second
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter_per_second_per_second = _np_.array(meter_per_second_per_second, _np_.float32).flatten()
                if not meter_per_second_per_second.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter_per_second_per_second: invalid array length: not {meter_per_second_per_second.size} == 3')
                self._meter_per_second_per_second = meter_per_second_per_second
            assert isinstance(self._meter_per_second_per_second, _np_.ndarray)
            assert self._meter_per_second_per_second.dtype == _np_.float32  # type: ignore
            assert self._meter_per_second_per_second.ndim == 1
            assert len(self._meter_per_second_per_second) == 3

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
    def meter_per_second_per_second(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] meter_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter_per_second_per_second

    @meter_per_second_per_second.setter
    def meter_per_second_per_second(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter_per_second_per_second = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter_per_second_per_second: invalid array length: not {x.size} == 3')
            self._meter_per_second_per_second = x
        assert isinstance(self._meter_per_second_per_second, _np_.ndarray)
        assert self._meter_per_second_per_second.dtype == _np_.float32  # type: ignore
        assert self._meter_per_second_per_second.ndim == 1
        assert len(self._meter_per_second_per_second) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.meter_per_second_per_second) == 3, 'self.meter_per_second_per_second: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.acceleration.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter_per_second_per_second"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            meter_per_second_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.acceleration.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter_per_second_per_second=%s' % _np_.array2string(self.meter_per_second_per_second, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.acceleration.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8j<tkh0{?YaNpBp-6(%Wh7qwB6Wl@$(jxCaj*ygU06DLuq5OT^I3tAi@i#yfb#i;^&OI0<=F<>A*BoKiH+<-cOeu963e}aJo'
        'NshkfV&oDaCm-`(clFFrrUX#m>ssD>^_H({{&e!M|C<@A{^f6`-9QJS<7%!X3+1QG3%TR^Nt7m98eZlzkBrKElPUhVoAUB`x%hec'
        'S-Fspx-pAj{+*2N`7Cy{bTo@n*v)*Ohg>luli2x~`zBFqWj^8Vaiw9X6hry=$5wt`(qTIEm-6#6pLUrsN_v^$y8Jy@c!h7hRb@W9'
        'EqNI9eVTFuW|(WxQ87{viqZVKb<xO(JCC}tFH{oCPkHbd2DAaMOEE4c8&AY3urAKp?X$1)BULhzM(%+hvrl3zJ24MFhz;*>bu?1b'
        't|yHf^0;F}Nn7Bh&$Mx)Bmgh3=9eBcig25=1#|at3Pbbf@?n`@aKXnoU@90?beMT?wCPCtD$(3e;-Jh=x<TTXPyaJAH1t?-5@(Ue'
        '6-jo;z$#6QV1@{`$4Sbx<^j<%_Bqi>#0gViLNV1P5q!pm$QagFD~&USO6@o(O_c1w^n!G_bF*570VW>Pe33{^0=^?5CM4x*iKS^M'
        '{kkLws_`?WP)~0QTFNw^f<zII6UG0SL2h9Cj!L4wcHK)~rHn-27*{um=Db?uC!klSa8Ma{U{vi%I9uh4tgKJLDZsfs7G@m1Gzp3M'
        '9)=12+X<8X+P~iX#^w@)gzU=z{Nz3ZAK#mrB4mlIezLK7G_tUqc}Zr->S}9)bU9P{CfOI#7dQpI5u2_<?vTy(O6R~{@H>OrQDi^K'
        '!T=0`1wyho=04Y&DH(Qa7oZS`G`i<4gblWVx0sO)uxdn-X<SvAhv^^#6@-B`P|Ob`#49#X$HZ4sOYPK$*$SZ+q`$Ovr%e{(#E|W~'
        'iv%hmhFB`F=Q9OGk);@~Tg2-^lcL3xb;E>JIfg_5Avl%ekDFAH2;J|%Vl7x0VurEYIw4=Gme(eBct21Phk?3AO)n2n6!Qkl0%M?X'
        'HipCy2%>gMXoS=G#8whxo0wkTiCJ;YO4n&iyd~bIL)cGZzHXiICvDpP=-2I1Eao?U!&UOK>8jo!Zy1f;IN6V#G9Pm*hsykoh7|Zg'
        '3I&H`c7zfp9#-|q!p0x5kx#;reH_&=zinlh&xe;w^h|r1$Me|%9(28KO|y841#v~JiKPq(CE#Eb+KC6{VSd`(kq10*F;T7z%65Lv'
        ')k&s&4ih1FQwDUAk0XTAEAz<*K<x()aP&FQ)9|}M93nw3A4z4IPi=Km$kkmQC1pOBW*#)It9U01(O#cn;SggrvBG|gRheHqmRy|`'
        'XW7AEl?Lf-))h>HQ`r8lZP4-%lJK{7-SB9EparZJ=>J3k8(@&JZlS3eG_2WA)b3K%5qiL8m9xqyREiNtIt&yfVODcMMFD*~@F8SJ'
        'K#xIGlL!bdu!gZ-y#zD?J2fm^_23??Nz{@~xi5F*K%K({vCAFgVlRXc-Dv8hPu*~6^YV9@pZbL~A6DOwc&~`_6K;~0IeC>5-Hp5i'
        '@&i%55BajB_)&_tZ=(8F(3tBBX#Z0DE<f{t1;~xxTO=6HwzDt<`hR&=Y<y8J&{m;6xX9C5LrEtx56&6M7_T)D*Z~UTc(p;bpi(-F'
        '`-TcSV(|pxNI_59?@`3zf{xkoaXUU?ang=YA&wPv+O9u^I8o3U#FGU*ZP%YcoG$2DJAV#ww4mp$o>|261-*cHwxAagPZ#tO;;DkZ'
        'hB#Hw%Xa_k*6tN+XU^)mYVEy&I9JeXh*t{wCgSS_C5V>`dL8k#g1&`#sh~eVyjak;5ib<<9mLs!-mrenBc3bhg7t3^@k~K~X#M;V'
        ';!HtrT7Q@9c^&KbyNHtoUAF$OAdVMw)t+O`#$(-{r^@Szf^OP#-Lmm*+4J45^G@Hh_+yJdvG~5lpIZEx#h+WeXYr{;Ve!D?Gm9@Q'
        'erfS5i(gy(#^SdYzpL^7#IO}EH^M?Av>M@FBRp*c(Fg~P@T?JDG{TpS@Kqyx-3Z?_!ncj^ofR^8-NB6j_XtwE9rKXb;l`OX{rBc#'
        'K7<!n|CKrSir21EtP5|zZKU{`AMW7L(I@7N3omYbm)W=P)qHXr?qzdi6<mV^uEA9?{|vm0SO;E28NNZ^&*#_HmseY>YwMevYpspd'
        'R%_#SYh~ru^7=|^ZN0U=v9fu4bz^<KzNVn*C*cX3GGCf*Nl%C;;%QA1zZIVhaLM_HJmp3n&qyQgE^cL_Gr%vTs3H~8KZpqa;?K&4'
        'KeYIJyBEi~h{K!51)Xlq?E@l2R{RsLQE>;|_=h+r{ww~KiLFC%w=I4t?k$K9#IFPuABy{;osVd^@W$%jEkMD8zg)`vto`kB^!^f$'
        '4$;K%hxU8YU?48S+XOG`_*izvU?MrgeTYAMj@9OhT{>JvrUj8{VPvX+h<|g9qc33eMSpY`nfZIe7(M6z^Cntc{S5#B'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

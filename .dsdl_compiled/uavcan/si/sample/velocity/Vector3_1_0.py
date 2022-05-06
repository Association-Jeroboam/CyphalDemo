# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/sample/velocity/Vector3.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.468987 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.velocity.Vector3
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
                 timestamp:        None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 meter_per_second: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.velocity.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:        uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter_per_second: saturated float32[3] meter_per_second
        """
        self._timestamp:        uavcan.time.SynchronizedTimestamp_1_0
        self._meter_per_second: _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if meter_per_second is None:
            self.meter_per_second = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter_per_second, _np_.ndarray) and meter_per_second.dtype == _np_.float32 and meter_per_second.ndim == 1 and meter_per_second.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter_per_second = meter_per_second
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter_per_second = _np_.array(meter_per_second, _np_.float32).flatten()
                if not meter_per_second.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter_per_second: invalid array length: not {meter_per_second.size} == 3')
                self._meter_per_second = meter_per_second
            assert isinstance(self._meter_per_second, _np_.ndarray)
            assert self._meter_per_second.dtype == _np_.float32  # type: ignore
            assert self._meter_per_second.ndim == 1
            assert len(self._meter_per_second) == 3

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
    def meter_per_second(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] meter_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter_per_second

    @meter_per_second.setter
    def meter_per_second(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter_per_second = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter_per_second: invalid array length: not {x.size} == 3')
            self._meter_per_second = x
        assert isinstance(self._meter_per_second, _np_.ndarray)
        assert self._meter_per_second.dtype == _np_.float32  # type: ignore
        assert self._meter_per_second.ndim == 1
        assert len(self._meter_per_second) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.meter_per_second) == 3, 'self.meter_per_second: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter_per_second)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.velocity.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter_per_second"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            meter_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.velocity.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter_per_second=%s' % _np_.array2string(self.meter_per_second, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.velocity.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?Ya+io1k5#>d^ixMSDvMkAR%W*_95y!kOwQ}Ml3Kc?5TPs1L6(xu>?wM(BH#E0Q_mErz2I7YVA~1jlPzTT__!ImI'
        '27<uOn?E2AM)HzJKc;H7XLl)60;p5dm#XUOs#CpxIq~=Z&JI=oiZ|0vpn}kG70)CK<tNMwx#RjtlqO1QZi?AQI?H{XXMCrVa`W6Q'
        'eP%v2i^Z55vk2y|<!sMqv7@A;Sd_x<Jsu{$)E(zB_jQu3n_|-4<C&64Y{XD8@z~1G4IQRKe>0z%V#Z}!XVS|xSLP$o{tCZ(t4uMr'
        'EqNI9{h4+HrkShJNiotL6k|R2w2Zj(s1y4lOJey64|ZTcY4F&H2{BcBB2I#JF=w~Wzsip^labVN5B!+_Fjlf1^Wgnh^ES_pMrp?N'
        'q;^9dx3w^|310e4X*Ws&@bXG=;X$nkw>eudcMqp9G=DV@O>xczALD>!!JwkU+=HXdMAFX^#r-4>OmV^u65l-e&&bfwj^HHDBade!'
        '*(C$36w!idBG?`$DN~9EM9J9aL?sa?ECUl6%Q_^2&sY-~!}@BacBWCO9S5aJCfhK*C>`$Hs8(TsiN_RQB2tln?@EXXNqM%+(lnGl'
        '({SewK{bA!WvHjO1uf-@Ps2qKkCTl5IfuJ}?YmhL^|h<s^;OD91dj3S22q?>i~I!isuT_?<2H<DdlJr8xgsm;({KuKZjXgIM=y0k'
        'V!nrAg8z2IWWVcQZ@#g)3?U)=G5|lh&%nobr>6;7CTo9cY#xm)EN5PlYqGZ1Y>*CTnYuyth4ckZL0!a95#%=6+^BR8>;=Db$eoPr'
        'CwUlvA+SJ59>?70O0i6aovsUz2t;bt^A^Ge+rV4Akp@`RBFPo5s?5W5kb?@sz#1s#2NL2HYsh2bXHrS!bPux?LM}*udFytIEXIi@'
        '+jo`-WI_zF%)p+{GDwO%#dzH$UI&U4EvBp!Cak(+xF{e4r*eF!zA6%-`)ydP1PepFVNADn$d{|-T@$;!AE=1KKsQHq?;ap27Br>>'
        '#vsGl7%qlD5S3$~5Ka}7TS<&%qI-2G=EYSjU87C$mUx>EVLge3Zs|;X*rKibziSz>R9yc9&ytr-SNR6_hS7K$C;PEuigCAc$P{nX'
        'q`(hSNH`?3Ba|@tu*y#s*8Ye_F$G8Vaa6(lwv}PN7+x{xneuXv7xM!==z5(l#o{Rz#U-&WmUAGKfP+yeCmxu?;*`594|w3>MY%FC'
        't>TQUl05S{OoZG`8PG*Bfe=d16jKj?)(;-w=yRZ_;dg*IM1nj%4#@)rWs1?Z)TWr;>ZEXMcX*VT;&PgMP{MA;+j)qV`&<hf#=8^?'
        'nlNgnxOyzjI;+l#gJCloiEZ8$Oo4ky1g<Sra|qY*k5;$z(E>pWm^Z)#Nd~-t;l>Px@@7!FdOyjYE?2do25eThR~dzz(c(z0fr2E='
        'yKGRALEjF12-y};Z4loi0;&tFVa!}F0ZqVDH6K^ixCd*JY+0q;m%DNx<DpeN<qop47ea`x*BR3%aX7So`P&pHe=YR~)%PRbOXp(L'
        'O;S^kS1D1Q$V=dUAgcG^zAQc7hq`3YfBVg7-1P+zfe{}SrysBYS@H*qgom@OJPe@`ygVx!pPNP6ER_c>J?&~RbTaqgoRN&N!GXXI'
        'P?*3b2iby3=`ijaD(Q&DQN)pwp0M9zh{Givx8oCbeA42S9iK)VFX@b3e-d%Bq_c=8N_xt!KaDt3(m6YS263#UXRV%j#Iq$mhd5W#'
        '^N6QPdI9ldNnb;pF6l+P|8;BklC^W$>bYX=y@7bSq*oCymGn)-*GozeFP8Kg;%g;+3-Llpe}s6xq;DghE9s9B=SzCs`n7;~rlgD3'
        'za_-eCH;x@^QVZjCB0$&UAE_Stl#e-PL*`U`oD@eQPMSgj&&Q44SSyIUPnv1Y0q`j#<ywDcdL8v^j(WTv-oq1?^*nX#a~+dmBqUj'
        'pI8(Y4=g^j_`>2B7QeLkmBnu@erNIfF5a6Qw!+0)SgeI+E!?ezC$%7I;h+|t)xwKf_@WlRtc9;?;oDmHt`@$xLJsdd=nc?OkmT){'
        'hZGOJXG-^9o=e3Lwy^$t^YSa+y;;UO@EY7kvhVW4Z5%rK*qn8F$nk|{U%^+3scq=c`p7D1hy)tqnpk)SUPi19Z=)Pvqwf_9>l-U;'
        '&9(K7&CT^@W3Ab2+-k0_-dx#OZLV)LHyW#(x7HdP8{LKlMLz|P*_7c^-_TL<Sp2?A5`Pr#0GFJ7$WyN6@r*R$KE<t`5Ci-|$|_P3'
        '{aD2Cmwak!{!rqdtzI1GA`Y(~7j(Mz4J?+#H_%1JZM6NhI3xZi{*{ZZLvg1iek1NKiuc8D1r;BNd!i-o7b8kS^XmR+fu>ylY%#^0'
        '{o!)7Wr>|bG;sVmgPt^a_Ve&C!A>0?OUM{M<YQ=o_?zcgZ6Aw}4p+fwLNJ;bj4B4=-(2D73mART9}SU=e=v*zbN&z9MC3j84FCW'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
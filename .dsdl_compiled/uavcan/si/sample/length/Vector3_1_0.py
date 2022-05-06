# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/sample/length/Vector3.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.491425 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.length.Vector3
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 meter:     None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.length.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter:     saturated float32[3] meter
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._meter:     _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if meter is None:
            self.meter = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter, _np_.ndarray) and meter.dtype == _np_.float32 and meter.ndim == 1 and meter.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter = meter
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter = _np_.array(meter, _np_.float32).flatten()
                if not meter.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter: invalid array length: not {meter.size} == 3')
                self._meter = meter
            assert isinstance(self._meter, _np_.ndarray)
            assert self._meter.dtype == _np_.float32  # type: ignore
            assert self._meter.ndim == 1
            assert len(self._meter) == 3

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
    def meter(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter: invalid array length: not {x.size} == 3')
            self._meter = x
        assert isinstance(self._meter, _np_.ndarray)
        assert self._meter.dtype == _np_.float32  # type: ignore
        assert self._meter.ndim == 1
        assert len(self._meter) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.meter) == 3, 'self.meter: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.length.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.length.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter=%s' % _np_.array2string(self.meter, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.length.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?Ya+iw-e8TSR>F*gGtKwwByY`1vh+cAf<X-iEl(g_Cy4y9Go&Ft>@%!s{pXV&(K6sdV=g{76U5>tskA%8;tgh*A@'
        '_AL*6>_gP2KIXCCw>x`|O#sRKzMac=oA3M0oIf4=>%V7*s(;1Rv=^u#bX>(V$wK)l^Fr>peiEgLlA4=h_L0tVU*{R$?xoy3H;bQ}'
        '&&)zG=Ef|7`KvkG^;zsF=_nSZush^&R}1Gc_jQu3nPSr2<(ZO6Y{XD8@z~1G4IQRKe=(n%V#Z}!XVS|xSLS2T{Ti?Ot4uMrC3zSO'
        'yqR_brkShJMKMwjim~FFbxzBOJCAy?FR~<-pYmWE29ySWjhGNqjVIzbSQn@4_PN*jk!CWITJC}$b05V@c4HoV5NqD$+0h)$xSrH*'
        'oex9X;HA%$cB3Q!FE1D8A2f<^o3jaX_izeR^JnwW6lY!VF%DQ399DFYdl1@8B>gN=+)v`b6vx~k@y(O}jtmWL3r^xZ@_0s)9dc-u'
        'B3dv_1l#2#WlHgYC>i^ls3hWqWndy>S&u~U8EYbASYNHw&NM2u<DfLjWEZ9vq{E#X)hbLd@tER^L@E;S9SJ!hDbJQznugM68qVAy'
        'sK(E;4E6N4pru^#X*ek2agy;r=5RK!eJ4wzfp*nDzDgO1z%icPAd2&9k)MEGl|rC0?!sucD<QVZ6<JxIhA6<fT^8mXz0?Vb`7Wjj'
        '{@V$Yz1qM2d~0I~QbP7*0Df|xfsgM^PZP34R{zl2IGR~l&b%boWOcROB0bJBb%X2)=?k2Ku84KdA-BoKdZqKwUhq4I+R4aXl7|5p'
        '0t<xXam;<L6w74Tt6hLXAX2Now~#j22HxU{w7{wsNv?2JWge!398?en)<7}emyoYmLmd-8lS(S54rViiT9E$I=Istyh!ah=?kp0h'
        'gcx#}fjysPP!xHJ`MOEG9yBRhOj$2XSars5P(TGv<@k1UR3t+8yRcXZ7KV7jSZ>{rFICHH6FYp6sEETrU8A~x4p0>H8p{H6kl}0$'
        '2SXr<$}!LgCyL3<B*r$;{k{`(;)<27(YAP7yhDeupTvCKIujptXy^WKIz}uO*MG;e<Ym)Uy}`L*HlD`GUhJ4++^rlk#aj(2@ck4D'
        '4$15YB}_i7>XU_yKcZDkLC8LiDwyB0GRzml%LYADUheT??hp^UUauxtjAB7t6l-EB2SN!r7=?D?fjKBnxI1#62QD6zD+ALhPP;0}'
        'GoQmm$la6yT@(`tq4Z2K^#DkH{{fCZ2YMQQ7l=b7$l~KrJkU_480|`Jis{W>3a565M~NverMU+!>}I^1hiG}gwXk8lrdZH~Su@3z'
        'SJJGr;w(FuHlvZ)=3K!PxQ9gG+Ez6Oa2$W@)UA&e2wK3p0VYT?-~~)KRxq?TgVxo1N%nN9>J4?sW_5a%QK%U$j`SKRNW#2kgNh6W'
        'cHl$Eu7GZX{3a1lU0@Ak<$4Kd0-kF4xa!7TSd(N+D&@Z1k%uZCu8ODJL00xcNYVACVg@7*LF<>lO>z8}Qh!)|KjQszE=JuXH3fN{'
        '64i^m1kMMtdJoRa(&K&TO9uDv;4&I_eE~#Z#K*<S2P{CA{N5tr;cO=lL%0ZDo)xVx%mQtf%7ZICtu+`rnR^gtBxAhbKw$eQOyDI4'
        ')q+atFzy>F>4?Qq#F3I7v)^Ng!zCTJ;}dp#(&CgIpGF)n>5N@}9C5Owvxvt^dcv+hi8xczQ+EC|;#f(~SUq!yXG(e&@l;9AA)YAd'
        'dBo!-eFJg2q!;Y|H?7@^*3KoX=d!i;7UHFnUO~KA(yNGXmXsh~DCsrCH%j_8;`x&P0P$Q&-$6WE(jOwumGrvxYaa1*Nf)eti-;#n'
        '`XlS-j}d1}dc*p=WaD+L-|r$$m2}zqzk)bX(p4MBn$5?$ji)--(UNZ1xNh3~wrza3>T{>>S^SB`pIUt1;?FGp+~O}R-nIC|qOiDc'
        '@tMUJ7QeLkmBp_ueq-@li{I6FZ*tfQ7aC!q5!#J#w-KH+f@p;OMtIf;FB;*?M);}`zHWqX8sXbU_|6JByz}60fExu#-i~=l@o@J{'
        '>A}l$u^7TDZ1CQ^^qO~Xma!hZ2DgyxYks(mLq{K*vn~%gzR>I|_;N9|1vj)lvI;Il0vF<{n12RdMyv~Oqa0tO?-%oH>&vU{)wT7F'
        'jkR`bwcT#rYOk!^TwY&kudTP&TPqv4R$J@q^@RmZKLwB3l=)Kk3>_7Z#cykp_`Prsamks7Jmp%xnvq7_r?}M<;t;=(vdUCMKM^tf'
        'C7+pwKa}`;r=Q2Mh{Nj#awz@@SEsm*2LB;Wi~os#<zn+d-06s4iMtEp1MzD?#fRda=!pBph>~z))xT3fun+3ul>M!8^p+Ca2dMtl'
        'p#^>EaJc8-ErOSG{7MeSlpzJft%pBzUa9R95z^r*{x-zl#`vqS#ecZM(HAiKVlWya|9)>6bL9LV)2T7l=M4Y='
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
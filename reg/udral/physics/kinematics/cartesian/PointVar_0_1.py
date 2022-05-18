# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/PointVar.0.1.dsdl
#
# Generated at:  2022-05-06 20:34:35.343647 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.PointVar
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.cartesian


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointVar_0_1:
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
                 value:          None | reg.udral.physics.kinematics.cartesian.Point_0_1 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.PointVar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          reg.udral.physics.kinematics.cartesian.Point.0.1 value
        :param covariance_urt: saturated float16[6] covariance_urt
        """
        self._value:          reg.udral.physics.kinematics.cartesian.Point_0_1
        self._covariance_urt: _NDArray_[_np_.float16]

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.Point_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.Point_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.Point_0_1 '
                             f'got {type(value).__name__}')

        if covariance_urt is None:
            self.covariance_urt = _np_.zeros(6, _np_.float16)
        else:
            if isinstance(covariance_urt, _np_.ndarray) and covariance_urt.dtype == _np_.float16 and covariance_urt.ndim == 1 and covariance_urt.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._covariance_urt = covariance_urt
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                covariance_urt = _np_.array(covariance_urt, _np_.float16).flatten()
                if not covariance_urt.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'covariance_urt: invalid array length: not {covariance_urt.size} == 6')
                self._covariance_urt = covariance_urt
            assert isinstance(self._covariance_urt, _np_.ndarray)
            assert self._covariance_urt.dtype == _np_.float16  # type: ignore
            assert self._covariance_urt.ndim == 1
            assert len(self._covariance_urt) == 6

    @property
    def value(self) -> reg.udral.physics.kinematics.cartesian.Point_0_1:
        """
        reg.udral.physics.kinematics.cartesian.Point.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.Point_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.Point_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.Point_0_1 got {type(x).__name__}')

    @property
    def covariance_urt(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[6] covariance_urt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._covariance_urt

    @covariance_urt.setter
    def covariance_urt(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._covariance_urt = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'covariance_urt: invalid array length: not {x.size} == 6')
            self._covariance_urt = x
        assert isinstance(self._covariance_urt, _np_.ndarray)
        assert self._covariance_urt.dtype == _np_.float16  # type: ignore
        assert self._covariance_urt.ndim == 1
        assert len(self._covariance_urt) == 6

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.covariance_urt) == 6, 'self.covariance_urt: saturated float16[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.covariance_urt)
        _ser_.pad_to_alignment(8)
        assert 288 <= (_ser_.current_bit_length - _base_offset_) <= 288, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.PointVar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PointVar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.cartesian.Point_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "covariance_urt"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 6)
        assert len(_f1_) == 6, 'saturated float16[6]'
        self = PointVar_0_1(
            value=_f0_,
            covariance_urt=_f1_)
        _des_.pad_to_alignment(8)
        assert 288 <= (_des_.consumed_bit_length - _base_offset_) <= 288, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.PointVar.0.1'
        assert isinstance(self, PointVar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.kinematics.cartesian.PointVar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 36

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8TZVOF0{`t;TaO&Y72f;B_x0M2g9(fYF>A+e_r0qD8xtF2QP?b(tXGPhre>zR)l1KGtGj2l6UkC|NMuVbr6d;;zku+Z2V{as'
        'ERq0kNJx?V6Zi={a?VV(cWv)J<T<<2_IIl4)H$av=Th^>iI2`792xvo&u0C0(N2u0;CalF_z$d^a3gA^oh&WllB;U(yJg;MmA#z5'
        '*Uz}Rt4@BXZmET8GU~DpjGxW<iqUK5EHN_CFXC2Vd=Phehm}aSSYGlXW?f@3jl1O%%T+ZKt?|5w)2<RD)%234?<zV%NB^uoRMqZ?'
        'm1Q0`doWeq0A1Ty`H)Lhlb2(jv^T8V6}4H(q7qFOW5Z4{S)Kl0j8$S<%+^MUJvWp%pasou5_!DG)><&7h>c!1E{%kDS4v@AkK25S'
        'x5_kkhH^&f$dhuaW817O&skqphc3tKy#3}t;;Y#8=n?FVc)~lpTMpN`-8N-;+=<J04LD{mCn+l*m9jf(#$_}#ThR-!buCtuQ73J~'
        ')}5-3EY{O;nsE`vuHq1$*PqloU}RL3tlMUJd$XY1Ag9AtU`KjwRD3gMtrE_;fb+ksX^^q(jgE|1K^XX<V>vGIZO8HglUS~22d?b|'
        'jun`$<M}~I%)kWnY>&8Z82VmFLMw0spO`qu_RWBprcFGD1itB!(DR7z*n#hpfLMX$xu%P~j%T?Jv0Wd;yN+!+wogb1O^X0CaX|(A'
        'n~vuMp5=$cH$j_adV%kGmQ8Fk@NL&~L(>dRhlGv|lU*|aWyCXy3rvm^f^5|0*p3fewrz(lv3!r1#PdQ2wAv1=7M2K0C$?{!uI0J`'
        'EFO$?z}mnfW@v?W7!qRHo(Z;_wr>&FvRwjleWGyld(CPVjw@rWxa=!BUQI;J1h)7@eG@iL1TIDScw1F_eiN6&`}Hm~^_{53qcl@h'
        'V>=;5ztc>UxTUK3tGtuKJ;T#{E8{tX`@V6rrlOXJ!7IgU)xmdo#>;qXzOm>7uwA?XeEYBUl7!{`$C*IZ8cTXy{Y5R%3$kd!$|s^u'
        '+*R~G5^NobX}q<)grQVAimW4&j%gg%IH7S8aZJ)F-JV7qmvlzAXLWm*=G%=pDd`?Pz87(qr291PN8BUn0X;sa`48&;c`fIVZXee2'
        'k02h9^k;}Ok{;Fbe~vgO=~G(%G0p!p;!#O|fp}2TXSBR$5vL?===sMHk4gF*;t@%IspUPd`G18tE$Inu*9(ZxOS*vAkn|+t(~_Rj'
        '`hJagNYc~V-ZNT`q3u44I3cO2^;?K%B()JwN$McJAgQbMc!<X(^%0+uG|=`EtuI78Ea{7Soi8Eom-J<=_Z;G^r04azU(x$>LF>PQ'
        'XiB=Q?G=d2lCC3Ok@Pkqk@RE41xY{EdhhA=e2aKr(gzxU(D>sJug;8W;%H4Q)C8%CD>boP6QU;8YvOiId|VTs*2KM<__ih<)Wi=p'
        '@uMbs5ODc=#=3)Ss{5MgD3GKkJG|tOdMBcG3T`_BfrC}^o6>C5><{z#EhX-W=L*OQZJy=4#Y)~*cdC8SO-w~mmgZ#?x7D?3E-KPq'
        '-r_Kj@F-&t^Q&ouByK{yUxe~ueGz-_f`^Zu1>GXWdSNV!RkiD4KNBpu1kpo54(v4{nnaMB!FNI5M(&1CHZ{zzFtLD%6PRP6Q)ij#'
        '(55_VScYj}#8M^ZrTIv(0u0MBK|)4ci(6dX5ub~{i}T{uK~xc!#Opd04}#AkYq#U>$`cU^Mz28Gk`0Fyoq<hVqW8sh_+Q?MH9N89'
        '|1H*t&mIpj!|aUS1))WJaZ9ZRP}zy63i0I~@sDfbpW>?p@h|aj@gMQE_@){MXNRhNP>N&R7#8CY7&gjr2qF&)a#igcl;q&x)`p9V'
        '@4%g_Qx|KlMk`Ho@KA^$MI*i0V2unXHR5igfD(xtYHQE`??dW)@nFZfcbt32xwm)jO^@IcnmQ>?Yw9dLAWY#3@3!zoSWUu{$#nHg'
        'MVzBkTl?RentBTu-VkpO8QvT2_P~TC`aZbh`{<6fHx}ZvYYz?F*GktIJbAlNj`VVPxPM-SzZ;Z1zqfBR8o$jTp`Xd)6;U=yWLrr%'
        '#)ney#>UJBgq=KIH^5Ym0c>IQ6O3SUt6u=D{uMsGEo0egh~qEf=Oz5SjGuGxspjh6Jhlj1+f^YOv1oH;a`<A}#Zs)h<x30SfcVgY'
        'N(X-~*-F~#C0xq`I{IjE8*Jk0-(ZXvFmSaoDz4+F9;(CP69c&M#!oNsARtK+000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

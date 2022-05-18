# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/TwistVar.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:48.323278 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.TwistVar
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
class TwistVar_0_1:
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
                 value:          None | reg.udral.physics.kinematics.cartesian.Twist_0_1 = None,
                 covariance_urt: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.TwistVar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          reg.udral.physics.kinematics.cartesian.Twist.0.1 value
        :param covariance_urt: saturated float16[21] covariance_urt
        """
        self._value:          reg.udral.physics.kinematics.cartesian.Twist_0_1
        self._covariance_urt: _NDArray_[_np_.float16]

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.Twist_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.Twist_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.Twist_0_1 '
                             f'got {type(value).__name__}')

        if covariance_urt is None:
            self.covariance_urt = _np_.zeros(21, _np_.float16)
        else:
            if isinstance(covariance_urt, _np_.ndarray) and covariance_urt.dtype == _np_.float16 and covariance_urt.ndim == 1 and covariance_urt.size == 21:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._covariance_urt = covariance_urt
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                covariance_urt = _np_.array(covariance_urt, _np_.float16).flatten()
                if not covariance_urt.size == 21:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'covariance_urt: invalid array length: not {covariance_urt.size} == 21')
                self._covariance_urt = covariance_urt
            assert isinstance(self._covariance_urt, _np_.ndarray)
            assert self._covariance_urt.dtype == _np_.float16  # type: ignore
            assert self._covariance_urt.ndim == 1
            assert len(self._covariance_urt) == 21

    @property
    def value(self) -> reg.udral.physics.kinematics.cartesian.Twist_0_1:
        """
        reg.udral.physics.kinematics.cartesian.Twist.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.Twist_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.Twist_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.Twist_0_1 got {type(x).__name__}')

    @property
    def covariance_urt(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[21] covariance_urt
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._covariance_urt

    @covariance_urt.setter
    def covariance_urt(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 21:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._covariance_urt = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 21:  # Length cannot be checked before casting and flattening
                raise ValueError(f'covariance_urt: invalid array length: not {x.size} == 21')
            self._covariance_urt = x
        assert isinstance(self._covariance_urt, _np_.ndarray)
        assert self._covariance_urt.dtype == _np_.float16  # type: ignore
        assert self._covariance_urt.ndim == 1
        assert len(self._covariance_urt) == 21

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.covariance_urt) == 21, 'self.covariance_urt: saturated float16[21]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.covariance_urt)
        _ser_.pad_to_alignment(8)
        assert 528 <= (_ser_.current_bit_length - _base_offset_) <= 528, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.TwistVar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> TwistVar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.cartesian.Twist_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "covariance_urt"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 21)
        assert len(_f1_) == 21, 'saturated float16[21]'
        self = TwistVar_0_1(
            value=_f0_,
            covariance_urt=_f1_)
        _des_.pad_to_alignment(8)
        assert 528 <= (_des_.consumed_bit_length - _base_offset_) <= 528, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.TwistVar.0.1'
        assert isinstance(self, TwistVar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'covariance_urt=%s' % _np_.array2string(self.covariance_urt, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.physics.kinematics.cartesian.TwistVar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 66

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8NVSAw0{`urTW=f36~`q~SDKb7$#PZOu~&{`QL;tdWh$-Hx^`TnV>znrI!b_gJ>-rx%PhIX?oySC8fYF`*uVlAz*`_6A+LQ2'
        'oCa+dy*fpK0tE{ABjh9GvFDIyM2Vqd=s8?K`#+r7xp0=hbIy$Y>z?0Tndqut;o0hr<y%h9^o3`0$NnWRI3i~j-E!6S?Lb7~(Yt|H'
        'D+V=B+}o*&=vg%NVe~l4hP`Hmm!W>v6Pvl3<#8uhl{>y&^m8BB6;b8^nnmsf!nb)PckdUrAKd3&6b_hM!t-sn63MQx|32BzBG$#a'
        'e;a)mg-1*t1fE@}LDT5xFxCOH+<htvdvDmnv6{0>nHCSY8Q_#<qERS&!%K&mY$W^Tpq`XW!$f3;dK%r+=h+(HDnc9I&ebY*klPZD'
        'TeO3n+<j3DTyL?_O*iY(-86d%PaW{ZJdf{0;qe>xwy<uA%4Q(1V$uFLaMTozD2qza_?ic;Qq{A|c3^M86N5J#mk0ZMIbs&<z;x<^'
        'M9hGdD{?<D%dQ10Hyxf>*Uhn6?i$psVHLiv-$Zv{lBOT<ip4!^Z%0p{pEBQs^{81m@FR~G19;6oy#5<xLm%Pf;?mqgeqnKGWo0qH'
        'ypYc?ujc3HFV8K_=NFgqOUv^ss|(9ZOLGy9RV##pFuN+p<&9V}>@f=t^msvk@#X|z4T9FsQJDUb9W<8nE_|dV2$QB;jY8v~PW+v6'
        '!FB9n6ppTmvJ1<KlYgfwJPxn7xsZKkQQGhuly8S4cSKbLcKhcN<_9o$`4f2V*zKC*aBrveA?Rz1J2eq~6lIyA`~rOQ9<yv$BK8ms'
        'zKupdzNDJNu~*iOk9H}RAWf3?koKZ>E7nJ!`%!xp8=%jFsC|m1NROZnD3+%BqxAd`YFe>l^jwDOhf$9xHbUj2G~RL4jACQd?gaJw'
        '9n>Dh#;N^xQO6WJi8`X#Db!<%ou+oLp$;l`hWbB?npDi7_7kXQ6g!7{TCvwrPbzjEbzHGGP){g!0rj|IlQd42<~M~pq}Vi#cM&zE'
        '*d?0p42_$kdC#II6q}>*=TT=BTR_bzwum~T*b?d`#g<VoDz<_;t=MJMDaG=rS;baSClz}W^@3vGLw!TB@1veq><a4ZioJz;PO%@L'
        'PAK-n#!rOZr0=;w^OdL%7276#Li#c3C#26wUy!~e{gU*nhOP~ClQFK1tTyu6xT%c|ZAfiwYvYMFKGw!3+IX&w7utBKjW4zF6&W?~'
        'FJimOEA`kxWd#HUJaVQi0^yke6%br>D^>*1SS}FU1wMp_qkH0uS=ea=vd58pF3<Vk4=qvkM3D!=ik^l;<|A~%X4Ulq)3&19;jrnu'
        'HLob3!VzYbgSQL&Q5?Gfo^BoD=Jq<4J_FdhXJKsVVxUY^?I=uL+o?+KTn9%If%mT!z_FMRlmKHGuNkz!tMxVF3N-YgVGqU@aGpB4'
        'L}7;FOKv_lmqXVT1?Z1QP04+jmWP1>BEgnj6wy=pnf!x%OJ1$J7kOR&m_kt93$1g@vMZZkb5&4#6QXssQ5~@XSl#>Vp?nwqHabqH'
        '<8;1lPDg&);%WLE$Q~i5m7j&@Zq-dg18Ue6Bap%<xYmvV=}%eY!1=VzASYWgNM1pI;F*WWB;^INrsO5EW|<-9<dR%|B3I<<VKXgx'
        '1#*<O4&xSC@6?l+pEe%2*UVHpE~4WiIxb?@MGSk~f-U9VYy^Wb<RS9&$5H9`-CbR!t8nw>AD_xU-Ijlrf62<f%D>6K%YVp!$`|qr'
        '`L8h3>JlRPZ;bZxKi?49|EI0eE$Cmq?8NU5oE<p#!P!q-VF15=wP80SI4`)hpdQ5QdjNxP3*T@bwS;veE4E=b0Xvc66oz<#TxUy{'
        'k-3wllL_E^73^ADzQZIW|54amKa;|JMB`KnHVVyiDcDr(o=ipIQ2lHQQvUg7(qDH2;gvNPPaJTD-0<v8+iJ`b5|PF0hF|4HVOZi3'
        '^lP<CPF~?e_H7x)uDKQ5AywL*h2SX-9)-Xb1ds39_V(Y7KkE3Sjz7}=sPr6Mgz%Av7<h;e!9${jhhz&6N#Y?vJoL8kkRl#Z#6!A;'
        'hhE|#O*|xshcxk!Bpx!v!$1oU!^A_1ct{ct<HW-V@sK7S`dWB6MLe7!9)^jBH1W_+JS2#R^TdNeJe(#T#)*gH#6yO7ND~hO#6wRD'
        '4>QEWH1RM=Je(&UCWwbK#KS4#VVrmvBOXSGhhxM;ns^u_9{PxfB=OKiJj@Xf8RB7sc(_SC<cWtY@i0z23=j`7@emUaG4T*<9%9Wy'
        'ta*qv53%MU);z?ThgkCvYaU|FL#%m-H4m}oA=W&^nul2P5NjU5DC|au4h<a|zV$Rvw%XhHN1?{{@fBx3nZ0K}y(`Phb4$&Wov~M)'
        '?2NUX>}2R<XKlS(zKb^iQuFA`PjBx|aj58SaSsyJqA+V-0CU~=0wUYbs*obiKu#(lpT_D<N9att*}{N)*R!|ZOr?xASK#rA@6;1c'
        'gF9|z6Y_D}#~RNKsJNc6V{zLa;MyR4kM#Y6%G-8uapq80YNNTA*u8$0daqq+L$c*rf9k<P>$utSw8yQfS^vR8>ixETZWz3E_fj9J'
        'O{wvXR~81U&jAK%)3~|6xs!zb&2VWGq;xlV(Eg_M8t#A2;O#8l47^RiEgaVWA)w7x=9MQJ&9c%gbXNaRS^(>S?M5k^sGopz?~f_<'
        'UvB9^l2Wg=Oagx0aMM*f3Vp2tf9<*d1NO*LM@S(600'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
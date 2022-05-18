# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/translation/Velocity1VarTs.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:47.963335 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.translation.Velocity1VarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.si.sample.velocity


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Velocity1VarTs_0_1:
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
                 value:          None | uavcan.si.sample.velocity.Scalar_1_0 = None,
                 error_variance: None | int | float | _np_.float16 = None) -> None:
        """
        reg.udral.physics.kinematics.translation.Velocity1VarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:          uavcan.si.sample.velocity.Scalar.1.0 value
        :param error_variance: saturated float16 error_variance
        """
        self._value:          uavcan.si.sample.velocity.Scalar_1_0
        self._error_variance: float

        if value is None:
            self.value = uavcan.si.sample.velocity.Scalar_1_0()
        elif isinstance(value, uavcan.si.sample.velocity.Scalar_1_0):
            self.value = value
        else:
            raise ValueError(f'value: expected uavcan.si.sample.velocity.Scalar_1_0 '
                             f'got {type(value).__name__}')

        self.error_variance = error_variance if error_variance is not None else 0.0  # type: ignore

    @property
    def value(self) -> uavcan.si.sample.velocity.Scalar_1_0:
        """
        uavcan.si.sample.velocity.Scalar.1.0 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: uavcan.si.sample.velocity.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.sample.velocity.Scalar_1_0):
            self._value = x
        else:
            raise ValueError(f'value: expected uavcan.si.sample.velocity.Scalar_1_0 got {type(x).__name__}')

    @property
    def error_variance(self) -> float:
        """
        saturated float16 error_variance
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._error_variance

    @error_variance.setter
    def error_variance(self, x: int | float | _np_.float16) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -65504.0 <= x <= 65504.0
        if in_range or not _np_.isfinite(x):
            self._error_variance = x
        else:
            raise ValueError(f'error_variance: value {x} is not in [-65504, 65504]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.error_variance):
            if self.error_variance > 65504.0:
                _ser_.add_aligned_f16(65504.0)
            elif self.error_variance < -65504.0:
                _ser_.add_aligned_f16(-65504.0)
            else:
                _ser_.add_aligned_f16(self.error_variance)
        else:
            _ser_.add_aligned_f16(self.error_variance)
        _ser_.pad_to_alignment(8)
        assert 104 <= (_ser_.current_bit_length - _base_offset_) <= 104, \
            'Bad serialization of reg.udral.physics.kinematics.translation.Velocity1VarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Velocity1VarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.sample.velocity.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "error_variance"
        _f1_ = _des_.fetch_aligned_f16()
        self = Velocity1VarTs_0_1(
            value=_f0_,
            error_variance=_f1_)
        _des_.pad_to_alignment(8)
        assert 104 <= (_des_.consumed_bit_length - _base_offset_) <= 104, \
            'Bad deserialization of reg.udral.physics.kinematics.translation.Velocity1VarTs.0.1'
        assert isinstance(self, Velocity1VarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'error_variance=%s' % self.error_variance,
        ])
        return f'reg.udral.physics.kinematics.translation.Velocity1VarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 13

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8N411v0{@Ly-ES4g6~EWuugjOgd<B|hl2Wi!y!aYlb0JOJ)F}!YFcce#8j<bn?)c8YesyNo_Kg&&d1wXFN?nPqls_SVLjHtE'
        'eX3NoNR|4~r>N>%r7Dj-XLt7AYht%W!oPE8X3zJWbLQ6vf8U&Gl>f3f<G!ao-?BAVlKJuz=J?#Q-6)77EfZd3N7fUSx=E_|MnC4o'
        'i(>w>;?rU-8@EFi!2UJGdsgZx=3BAoYw2q1sSJ6*5+oDFLhS<`h1NsvN3Klz?T1Wl=pvi4x46=<Q;0@3`OwfW3fiE}-xi-0*&&-H'
        'iIPs5a9unGnfquvI8|ihHzoJIp_VP%V+pepR9%c!i()(@Dcf>cXlZF_7R110%P429yUb^*5R+n>HfaMD5r;vzm@!|^j_`TQ@JVFA'
        't@VEB3KfO&6Yg!mf=+<-e`B<tJ+YF3Oym~WGy5RavKMmiR+#V}SG!|y$aZ96`#kI=qM%){)@3@egUADGFJ!0h)r{~nYZdnH;1;;J'
        '`J3W?k)5<b$IxTS8)fu7b-=Vkfpk@*xf_LEksY+X$SofIW318G5S)Z*;BZBvO)_#ylSHtD2)4yZ%(Uhn(K2*7(NVw&Qy@Yy)h7Y`'
        '3=<+lIA5MjtQImg>%cTpvIpC9(&E<T@)SClI85_-A~o^&CZw20Vy+fg9Q)F(GK?S_H&qJx3_d|gspc&R6md9F{8uT&20q_ZQ847L'
        '2jMH3kpL9q>N3%smxtU4`05x8m0=H7)s_U?N>yYjy#-c)a$C$#Ick|iB;;G@Cit`IN86QtgZ<9R0=R^1OAqwqE(0BJv|5BLkfo11'
        'E4w`l$C(qQ30Yd|c1WKyr7x3hAzgu6kia3NE_t7<ESEe-z6HHg$Q?ztqty365J(^-4MXm7t(lU3zfu7bfyhJ;v<0`pXP_-cqythD'
        '5v3YWmEvLBOMwMpAPpGv9SQyl6UbxYDygNmDq~iC$OY*xtiHcS=E5i;H$RvsWnG9P1@c^`ASu!q{dJ8veYor>F=l-~Vr7gWP*7^D'
        'Qt^#CR3t$4dvI6_=KC07Ot+rT7s}(6h)q6pRKQ`O%F$#H2S|!b38n@5K;do(fg#{TZ5414j%HJ<QHa+h8QeQ40T&H5PrKqBahW#o'
        'K8Y*U)tP*-M%V8Ce60}e?BXxDie436<{QKfz40`RwnMAPChSt7B740q3VbJqgu|k^t0YX_FY}Z6wLap#Y#K~<aTUwzO+&+e)?6%5'
        'Gwq}f&t^yJsqOTu0*+QJinqnPqLV^F@i+*D>%_g{d3My^lsnwBF;KSjinZ*xt)o=A95#Gz#|+9vHi_U%r^u%7LDSf|hpR83JT<RC'
        ';SdpaiLqD~S!=Z)L##gFK~!Yt<J5tRYeV};eUvw>)L_I!RaoJB^i`3)v1f6$+Sa0l&MFctXS23o8kEB8Z<`BRJcl6sVXeCGD1o2^'
        '%oe!+k%DS~PR6{2OU>ZICfkvEx=`K-JtDJ=St%4UB@w%B7%+(Zw5kDR2^h+OA42v7+%fQK6hMLVj9|=HCjw4To$4xF-oY(66R8Cq'
        'b60N4kvxY6@swLwiya?abg|BpVd(~=lUIKi+2Nna<aYUcoez>YJ77m~k&*qF=zict5FhaB9f+4Hig)2QvLsT&7BpeI0<M1{yzJOL'
        '=3#C8)*&HrcP;gyvG!lx74QA7n4{fXJ1`K$6^DXOr4HB`$Pn8a5NrpDNo;M9Ey$EM@w-M&#|$1o9LwoJ^LreznbQfgK55pc3{IQ%'
        '7UD!s51I3a5vOu`1o2=_kDBwx5D(>a#_S(Q9M9<q!)F%pL{3j4&gAqI;?bO*Mm(I;Gl;F6o;BaUX5^kTa?Tq*-!bxDM?9a?HxSR|'
        '^i9Oqa!L@-=JYMZGdX=5@pMkVi+C!h7Z6Y8^m~Z2IlXA~x`cQ<r*lTXdBkHmeaGneeZ(U<y=?SdF!owT?<<JYIbAgRw-G0Ex@7FQ'
        'YW%Tm?CBsL$mxo)>zeUz*VuQxiaWhw@LhvHFlh3E{?Oo$4F1^QhXx-R6b5$;J~Q~a!7mJcY49t9FAaWe@S6(nOf?O0wkGCkqFWOm'
        '*2JTl5H+z=6VGbm^P2dgCcdnRuWI6DO?+Jw-xwl==?*#q^bsuWX3fFE4jpGY8P1#StbvVdIIdpErf)(kO?J(W(76b7t{dXYGhiIB'
        '9t<%lj*UOfE?r$-T<R`eU0zwa+U+cLyPfOZcKh1ma=UwVxx3tHuUud1EH77`r4&CCa2OSAxY@QD7)4wB1zL`{g`)l}&WXQ^m#Lu7'
        '#qBk5N8FneKNI)Gy4Vm8#KUY%Lvxs@265<L^(bCs$Esm`cbOL-JxA{1vG`?GKwPmos54Io)aFR-IRz~ods?_>5zD5l8U}3xUm1IH'
        '>j_PpU~2;XK862VpB8l?(c({QuoI0`GXm9&Ydrl3PCwe?w8jdz|Go+9cr_AK&K!y8Uk5RqF)<W>gTRfibUKU6!>}CXN<|9h3V2+='
        '9FD1R;-k4TR#&Px&40Y~xTxdwWW3pEh~rO=06dw1KYIr(I{+;kURvdw54(T$>Vx(^eD}fIZRF)wWM_82{UDs}R|1;-@iu(T6se<M'
        'wb^0UW#uSa+hVouI@sZPJygkRMut{ey;flg)u~hVU>GL<*K@DTu+~jz%P;~&;le;HG;1IvSj9_)a0DM}Q8sZL=oH%~>$j?w?@4I&'
        'iQl)1|35|lRUP~He(CqmLHZ36=G$2}Gsrpths5wuoou_8F~_X`0JKms{R|KQ00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

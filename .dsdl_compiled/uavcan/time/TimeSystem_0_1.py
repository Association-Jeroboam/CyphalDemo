# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/time/TimeSystem.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:54.235249 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.TimeSystem
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class TimeSystem_0_1:
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
    MONOTONIC_SINCE_BOOT: int = 0
    TAI:                  int = 1
    APPLICATION_SPECIFIC: int = 15

    def __init__(self,
                 value: None | int | _np_.uint8 = None) -> None:
        """
        uavcan.time.TimeSystem.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: truncated uint4 value
        """
        self._value: int

        self.value = value if value is not None else 0  # type: ignore

    @property
    def value(self) -> int:
        """
        truncated uint4 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 15:
            self._value = x
        else:
            raise ValueError(f'value: value {x} is not in [0, 15]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.value, 4)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 8, \
            'Bad serialization of uavcan.time.TimeSystem.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> TimeSystem_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_unsigned(4)
        self = TimeSystem_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 8, \
            'Bad deserialization of uavcan.time.TimeSystem.0.1'
        assert isinstance(self, TimeSystem_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
        ])
        return f'uavcan.time.TimeSystem.0.1({_o_0_})'

    _EXTENT_BYTES_ = 1

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{@j&ZEG7x5SHuLC~ZoxG4zdWp>5I@pXCoBB&8o5C2oacNknQXg|h73jkJsJc8}dX+bR^A4=otBw2<vz>YwPJ>Fk|e'
        'YzKd+5Ypbx&fGK4%sl(++TZ_fHmZ-iS4>lrW)U@@1<S<GEY2XJiOLIQgaz;38CqQ?w$w117T{m|&tLgp`~$a6CCkyiTe8!H$;gTv'
        'q7nWKr^Z6=-4;CsZG@7ZH{9m;v-NA=ZFE<D_piLWO_{Y?#H9t}f5MPAfLWaKZv99=mM%dwY0504HXysnz0e{TR-EFA?eC-!6A5WY'
        'T9|;on$c|<3rjPQ6U%*f4TC4lSemO8Jl}D<gL$Cf7PZlK988$e%5VOqcRSQrCR3)<%YiP+n6JC_Q<jy8V2!3K@vh-<_m10YD;a$3'
        '0tDaYyR+4M-8KF`|FGK#!TG&9&dzba*B|wJoi-hIdhO@*X}>@6{9^~lN-C?QNJyvzF+wIlVx?@<yk-)HuzICo3>v~g%b6vq0weER'
        'l5i#`Xk`|N(j;dmKr&#3iM-pOvrImkvkm8k1`~>Vh3l=C%;Fx)=DG1bcWbO!5_S#Rk7jGMyOov?S(+G={Nx5EzL;~cIy&rN%0K+G'
        '(rAQ2YB_roIkYOrEJGK5MYy$vd9uF`GCC6{qJUJeNa@Lbc-p_>NNYzL9HZulLq!i(CND^pE=iQMOh|)70g+`MgC=TB&`B!;XiW`)'
        '3@L(iM*YF#N3Ffq0e(lV)|2Y{BSGXC|FBclAUk8zP>QiQM=w#g<fY*AxQqi!!^Ss*VFfH|)-z`6vXurFCc;9*WnB$dWtIl`IE=PF'
        'Z&koS;wfQiD&(ZfsRogX@ys)7E<z$!>>pyvqEOo6sWCQ%24=910Tu=~0`bTMBL+UqB90}Mj3CM3J!Xa)hlH@A$V5`{k8Q>Gcx%=q'
        '{GnSp_#fS{b2u2h=(G<<oqmrF2hZD`qfR?a#G}LIEA~tQi5M@2qXH7Jm-0laGf4`q3M5Ft8(`i#c(_0VZu^pE(Rf;GU_eFqUH&Ei'
        'lz+`1^KbdH64fLH91MIvr2fL)p%ue4P)J4Ud+shZs?-UfAp=@4)C#v5{xT7JcWZ#eoe#q9Yt*Kdebf%Fg5Yjg{AV~ps}o_pYqqBa'
        'XW28zm3JQ$WsEsf4U;kpZ(iynI&9QZjgbNiD2GeAj#|+{6z196AZ6Q>GlQ5y34@%TiUj-xlKRK!5`Tcb3c4bAIW=>mK~Ncqq3SM!'
        'G*xXA_7FVIp23c<rwQzt(kD@~gUZ8XXf^bzH7F%#9ND>iF0`XAWoW1<=xLl`W}nT)Xeqo1+g^Y6?(L_-zNnsuuuxsMN>$+<xhaU5'
        '=CMLrk(Xnn884QQa=!?<E4{oxHfVxqQ_oM_yMubR-Z;dIVC|Jz#`N^MmGAxOA9UCLGBMtsMIFI+x5^mv%!R~dSg`Z3*bEmF7CGQ='
        '1`%emx?p={99lK{58s&p3g!m@00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
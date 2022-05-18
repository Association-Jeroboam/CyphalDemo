# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/translation/LinearVarTs.0.1.dsdl
#
# Generated at:  2022-05-06 20:34:35.143090 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.translation.LinearVarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.translation


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class LinearVarTs_0_1:
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
                 value:                       None | reg.udral.physics.kinematics.translation.LinearTs_0_1 = None,
                 position_error_variance:     None | int | float | _np_.float16 = None,
                 velocity_error_variance:     None | int | float | _np_.float16 = None,
                 acceleration_error_variance: None | int | float | _np_.float16 = None) -> None:
        """
        reg.udral.physics.kinematics.translation.LinearVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value:                       reg.udral.physics.kinematics.translation.LinearTs.0.1 value
        :param position_error_variance:     saturated float16 position_error_variance
        :param velocity_error_variance:     saturated float16 velocity_error_variance
        :param acceleration_error_variance: saturated float16 acceleration_error_variance
        """
        self._value:                       reg.udral.physics.kinematics.translation.LinearTs_0_1
        self._position_error_variance:     float
        self._velocity_error_variance:     float
        self._acceleration_error_variance: float

        if value is None:
            self.value = reg.udral.physics.kinematics.translation.LinearTs_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.translation.LinearTs_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.translation.LinearTs_0_1 '
                             f'got {type(value).__name__}')

        self.position_error_variance = position_error_variance if position_error_variance is not None else 0.0  # type: ignore

        self.velocity_error_variance = velocity_error_variance if velocity_error_variance is not None else 0.0  # type: ignore

        self.acceleration_error_variance = acceleration_error_variance if acceleration_error_variance is not None else 0.0  # type: ignore

    @property
    def value(self) -> reg.udral.physics.kinematics.translation.LinearTs_0_1:
        """
        reg.udral.physics.kinematics.translation.LinearTs.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.translation.LinearTs_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.translation.LinearTs_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.translation.LinearTs_0_1 got {type(x).__name__}')

    @property
    def position_error_variance(self) -> float:
        """
        saturated float16 position_error_variance
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._position_error_variance

    @position_error_variance.setter
    def position_error_variance(self, x: int | float | _np_.float16) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -65504.0 <= x <= 65504.0
        if in_range or not _np_.isfinite(x):
            self._position_error_variance = x
        else:
            raise ValueError(f'position_error_variance: value {x} is not in [-65504, 65504]')

    @property
    def velocity_error_variance(self) -> float:
        """
        saturated float16 velocity_error_variance
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._velocity_error_variance

    @velocity_error_variance.setter
    def velocity_error_variance(self, x: int | float | _np_.float16) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -65504.0 <= x <= 65504.0
        if in_range or not _np_.isfinite(x):
            self._velocity_error_variance = x
        else:
            raise ValueError(f'velocity_error_variance: value {x} is not in [-65504, 65504]')

    @property
    def acceleration_error_variance(self) -> float:
        """
        saturated float16 acceleration_error_variance
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._acceleration_error_variance

    @acceleration_error_variance.setter
    def acceleration_error_variance(self, x: int | float | _np_.float16) -> None:
        """Raises ValueError if the value is finite and outside of the permitted range, regardless of the cast mode."""
        x = float(x)
        in_range = -65504.0 <= x <= 65504.0
        if in_range or not _np_.isfinite(x):
            self._acceleration_error_variance = x
        else:
            raise ValueError(f'acceleration_error_variance: value {x} is not in [-65504, 65504]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        if _np_.isfinite(self.position_error_variance):
            if self.position_error_variance > 65504.0:
                _ser_.add_aligned_f16(65504.0)
            elif self.position_error_variance < -65504.0:
                _ser_.add_aligned_f16(-65504.0)
            else:
                _ser_.add_aligned_f16(self.position_error_variance)
        else:
            _ser_.add_aligned_f16(self.position_error_variance)
        if _np_.isfinite(self.velocity_error_variance):
            if self.velocity_error_variance > 65504.0:
                _ser_.add_aligned_f16(65504.0)
            elif self.velocity_error_variance < -65504.0:
                _ser_.add_aligned_f16(-65504.0)
            else:
                _ser_.add_aligned_f16(self.velocity_error_variance)
        else:
            _ser_.add_aligned_f16(self.velocity_error_variance)
        if _np_.isfinite(self.acceleration_error_variance):
            if self.acceleration_error_variance > 65504.0:
                _ser_.add_aligned_f16(65504.0)
            elif self.acceleration_error_variance < -65504.0:
                _ser_.add_aligned_f16(-65504.0)
            else:
                _ser_.add_aligned_f16(self.acceleration_error_variance)
        else:
            _ser_.add_aligned_f16(self.acceleration_error_variance)
        _ser_.pad_to_alignment(8)
        assert 200 <= (_ser_.current_bit_length - _base_offset_) <= 200, \
            'Bad serialization of reg.udral.physics.kinematics.translation.LinearVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> LinearVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.translation.LinearTs_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "position_error_variance"
        _f1_ = _des_.fetch_aligned_f16()
        # Temporary _f2_ holds the value of "velocity_error_variance"
        _f2_ = _des_.fetch_aligned_f16()
        # Temporary _f3_ holds the value of "acceleration_error_variance"
        _f3_ = _des_.fetch_aligned_f16()
        self = LinearVarTs_0_1(
            value=_f0_,
            position_error_variance=_f1_,
            velocity_error_variance=_f2_,
            acceleration_error_variance=_f3_)
        _des_.pad_to_alignment(8)
        assert 200 <= (_des_.consumed_bit_length - _base_offset_) <= 200, \
            'Bad deserialization of reg.udral.physics.kinematics.translation.LinearVarTs.0.1'
        assert isinstance(self, LinearVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % self.value,
            'position_error_variance=%s' % self.position_error_variance,
            'velocity_error_variance=%s' % self.velocity_error_variance,
            'acceleration_error_variance=%s' % self.acceleration_error_variance,
        ])
        return f'reg.udral.physics.kinematics.translation.LinearVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 25

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8TZVOF0{^{O%a0Vt8J}I)H;;woWx#eBW7u`r-Ul<wfb9ean?M@Y1QtR}psDVzovNXyyVKRZyJN*td`JXROKypdLT*t`<Uim~'
        'K*}{rIOd2FDTgRge8?f+*Ihj`yUaj92`g=VHTC%3-><6rXPbZd?%q=N7r*T{ZD~82Az2`(Bfg-f!!*P48onn*$kKT0l`x2`FbddG'
        '(`V`Zbn2`0%XBgxFkISz`EtN&T4V>*(R|*N!jjq@;j#t|u^R@|l@9bhSGxeiG`L2CC7H&<#tI8045z#l4_#CJ`>9^i`+kvrmBwQR'
        '4Z}c~QOIO^69o29wY4gZ2hIxS*liU@4V#A42vKj|pAYhZc<v=N26g!mA1O5BTR<B=uGmd<Fn%YZD;9ONP&Al!rRiEc@Lcf)vzK5%'
        'hP2`5jQaFa7e>7d^aIflp;!R}C$73u)LdqtcSBZV!TN}d8Kwvghq<+or+O94x2Oz_hG&EMhvPk$3P!k1I|FkUaSD9i_w)2}8t*bd'
        'N7tr--O1=)WP)j94PgbIWR~aJX}sC6JuAKbm;O>|i8JCx4U+}LTP7W=BndeU38yQJ_*6<}6DeGa5$QD;p#g{pXwW1L`00j3xUfE3'
        '8ET`*RE+~uFAz1Do)j9>j%BOR!NjDJO%Wl9&6XifHt|_7O?}@HRvtZqY^*2<kWXt1N{S>Kg+LLLk%0Xqg4n?J<-lvSxyx4gGG?R!'
        'im~7rk&I=FED!if9}E?44Mu|%0k&nTh)nt@SOLndP$y!jW#|!?t)QErS$4eDT))<QWnmgzLRN(hdNPZGj;BUP37IDIw<-(kJqydJ'
        '=|v%#pRZO(6LM4@Bdc6k9H)GUT-eme$7G?L@$A?OdPk5u0a^7T#|A+lfsn{`nZ=}}fpD6+3XljygtDbAxDB>}wiuBLNDa9cNnDkQ'
        'hiN+k7KDN{V9eG8_{$9;kBJosDWsMgbH;&O5Z3gWj~B_L>xJa(CsQP=Io}IFo<##lipWQQogiitsvjl#wCQ*>i!lTWfJe&|Un)XH'
        '8mN8^7E4YY2P2H>R&&^NwmcWH%-W7>Fc`>lG;GBIlHzEHX@NcnaMp#u5OAW@QYeIN@$ebX#WD$7bq5e|MD?chDu16J(@R)Sd?qiQ'
        'p{tAf;%7fxO!-`V<Z~8y8%1aN2601g+;P2CS4-nTBU31i-z-3Zt@)5}h?46dVfb>EpVTSz;UC2#V6ugyh_h!^ALiq}*%URCW@NH>'
        'q61(Jvzfy=S~1HH@eg<<0zk1D2!(QDc6u+~W-N;}W*ZnNL)htJyu*-Q6j%%<9A@|w;36JE;s`U1M=rq;vUUka?*lyb%>Zz456_H#'
        'U!?KqnWhi1`h+#SG(O-*CKRp#&>T4^uMOQ`#9$7rupfPu#&2~6S8Yz4)zDdKh;TMxa4JD5EPq24XnGHV@cYHQ;86lW379QV|6TxS'
        'fKJA|g`%cVu;Ho~+?mcQLUzc^VwMSoObPkA3Ihh76Xh6?K|os${NSR-p~k?gUIPHmR)R5KO%FH$Iu$6K)!+)O@q%gTGfOOsjy#70'
        ';ttagi%kbybfn0WHgtp0;l|%-yyd$hypa9A!dgijZ!$bTjY%&ive_^_h!1%6BE(C9;%88eH1vY@5j1F69LhiCcD(%(wGkViS;Pg-'
        'E=G<6@V{}EfAn=asaF$e!VSUCIi&h<WP+Uy;o`9d9lC~{Aw1e3Tac;Vhx<y2-mmB;r2UD$S^XYB+L!2qYJ5nI4=XyN#z&D3Ci<9K'
        'zXj=VqHjgIInlSN_1lq-CHlCU-+^=>(RV676G(R^`Yxp7iM|`@wnX29bW5V|MLL@3`_%q7l-&JF&H=^eppy3{(gTV97SjER{x;G#'
        '5}hF3m+0>x-J9r#knTzJcaiQ+^utJZCHi|vCldXL((5SF9f>}v^qWGuJ<;D+dVUM()<i$1^qp4rYD(`Jq$7zwtMs2kI+W=1%8uj8'
        'A7y1v1?i?lUr=_PQ2wnd`%dO@*H0<>fubKOs`5hrwxZur^t7Vq6uqt}S9DF$yNW(g^r51U6n(7d6GfjY`b|zR4)>|fzM?Z(bgD(?'
        'T+z8+ba>HOD>`?J&V!=!u;@H0I**IalcMvq=zOC(5!~+JM1XSyp<Ruc2<&j;jD+p`=3HFDgR9$hb>=1S!T;qg_@KH4OQA(@7t(SZ'
        '(XLq3DR^{TfIC<mjz`YIAs?>0)xw!d;7mQmXYPW@4O#=15ngCNjgKBL&(2rpkCzt~j#n%5)oSHrb#Cs&Y<aGFyj(3;<`z!QSIXu5'
        '%*z}z&|q+h0jKakMJDCv0dM}!pGvOZ;};hBMSf|L|A1fSSNIaY%CE)!5{{|OXapQV>N*^6&kb3B*zg<okSV{(Z|5*(@#PlU-D&l_'
        '4vZs!aa<y_@eoXm;D6=Iw7?_D|FGDK=WzBG%ic<v=3U+X)&{q)Fvqh5+yh_i_`g2mYW}xZ^6z-&Ujs1RP)~&pSJ!v<l}hz((DZUR'
        '{|EnPJX|QA@_)Ss*S4kgcI}}JuBDd696YzMHeRE94{UUAFHcv{)7pzXy`|HR*W&FB5;Kh%YCKsV0B!l7>+hlFgV=nE%@Js#t~SJ*'
        '0KMSJpWzqYI&%brYh@e5(s--`#h`R^9D~B0+fcgk-iz?i$sU~4@$l~F5(-ZkEq#$EmOCyryWwqsmu0u>?I<3}FGp}6#qSx<=T`p_'
        'Sf2f;{}_6`*8lrOj;|kt-Av+&)3D<7vnyI0dd$~9Y;m{^D{eoBLyvhC{DJ&M(;0RCN4~!vVdS55k8=Hcm<8vsIgicvvC*N4cNE`d'
        'x<vEE`TMeduC;8ef{oQKUb@`!(gRrW;5lCEG2hKgT|s2L6GR3UDwWxC8zS}=M}@(Hzzg6N83^iH$S@wck>SU!`J3r0u`Zyp3+tUX'
        'CNthMIT%g7s*D4j0MSLxuJv+m%_~U?M83vU+EM=%W=Vq0Z?O3_HowE>w>{ycccSg;_-xq?IX=(cc=$yI9&Y)UQtA*Hnc0iaTPCeU'
        '9leT=Jh+&VS_H2+B9^n~e`X~qtVB+ct3Ct#uhaPdyuSWZ^uN^m*5`Si{+&n0I2;*yu{?xD58I21y&HzR?|lS|9zDBv!*KV#k73c{'
        '&b@hUt{=vd)cyl^2yHYj7XSb'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
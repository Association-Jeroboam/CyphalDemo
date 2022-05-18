# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/common/Status.0.1.dsdl
#
# Generated at:  2022-05-06 20:34:37.414530 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.Status
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.service.actuator.common
import uavcan.si.unit.temperature


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Status_0_1:
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
                 motor_temperature:      None | uavcan.si.unit.temperature.Scalar_1_0 = None,
                 controller_temperature: None | uavcan.si.unit.temperature.Scalar_1_0 = None,
                 error_count:            None | int | _np_.uint32 = None,
                 fault_flags:            None | reg.udral.service.actuator.common.FaultFlags_0_1 = None) -> None:
        """
        reg.udral.service.actuator.common.Status.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param motor_temperature:      uavcan.si.unit.temperature.Scalar.1.0 motor_temperature
        :param controller_temperature: uavcan.si.unit.temperature.Scalar.1.0 controller_temperature
        :param error_count:            saturated uint32 error_count
        :param fault_flags:            reg.udral.service.actuator.common.FaultFlags.0.1 fault_flags
        """
        self._motor_temperature:      uavcan.si.unit.temperature.Scalar_1_0
        self._controller_temperature: uavcan.si.unit.temperature.Scalar_1_0
        self._error_count:            int
        self._fault_flags:            reg.udral.service.actuator.common.FaultFlags_0_1

        if motor_temperature is None:
            self.motor_temperature = uavcan.si.unit.temperature.Scalar_1_0()
        elif isinstance(motor_temperature, uavcan.si.unit.temperature.Scalar_1_0):
            self.motor_temperature = motor_temperature
        else:
            raise ValueError(f'motor_temperature: expected uavcan.si.unit.temperature.Scalar_1_0 '
                             f'got {type(motor_temperature).__name__}')

        if controller_temperature is None:
            self.controller_temperature = uavcan.si.unit.temperature.Scalar_1_0()
        elif isinstance(controller_temperature, uavcan.si.unit.temperature.Scalar_1_0):
            self.controller_temperature = controller_temperature
        else:
            raise ValueError(f'controller_temperature: expected uavcan.si.unit.temperature.Scalar_1_0 '
                             f'got {type(controller_temperature).__name__}')

        self.error_count = error_count if error_count is not None else 0  # type: ignore

        if fault_flags is None:
            self.fault_flags = reg.udral.service.actuator.common.FaultFlags_0_1()
        elif isinstance(fault_flags, reg.udral.service.actuator.common.FaultFlags_0_1):
            self.fault_flags = fault_flags
        else:
            raise ValueError(f'fault_flags: expected reg.udral.service.actuator.common.FaultFlags_0_1 '
                             f'got {type(fault_flags).__name__}')

    @property
    def motor_temperature(self) -> uavcan.si.unit.temperature.Scalar_1_0:
        """
        uavcan.si.unit.temperature.Scalar.1.0 motor_temperature
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._motor_temperature

    @motor_temperature.setter
    def motor_temperature(self, x: uavcan.si.unit.temperature.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.temperature.Scalar_1_0):
            self._motor_temperature = x
        else:
            raise ValueError(f'motor_temperature: expected uavcan.si.unit.temperature.Scalar_1_0 got {type(x).__name__}')

    @property
    def controller_temperature(self) -> uavcan.si.unit.temperature.Scalar_1_0:
        """
        uavcan.si.unit.temperature.Scalar.1.0 controller_temperature
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._controller_temperature

    @controller_temperature.setter
    def controller_temperature(self, x: uavcan.si.unit.temperature.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.temperature.Scalar_1_0):
            self._controller_temperature = x
        else:
            raise ValueError(f'controller_temperature: expected uavcan.si.unit.temperature.Scalar_1_0 got {type(x).__name__}')

    @property
    def error_count(self) -> int:
        """
        saturated uint32 error_count
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._error_count

    @error_count.setter
    def error_count(self, x: int | _np_.uint32) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 4294967295:
            self._error_count = x
        else:
            raise ValueError(f'error_count: value {x} is not in [0, 4294967295]')

    @property
    def fault_flags(self) -> reg.udral.service.actuator.common.FaultFlags_0_1:
        """
        reg.udral.service.actuator.common.FaultFlags.0.1 fault_flags
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._fault_flags

    @fault_flags.setter
    def fault_flags(self, x: reg.udral.service.actuator.common.FaultFlags_0_1) -> None:
        if isinstance(x, reg.udral.service.actuator.common.FaultFlags_0_1):
            self._fault_flags = x
        else:
            raise ValueError(f'fault_flags: expected reg.udral.service.actuator.common.FaultFlags_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.motor_temperature._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.controller_temperature._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.add_aligned_u32(max(min(self.error_count, 4294967295), 0))
        _ser_.pad_to_alignment(8)
        self.fault_flags._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 112 <= (_ser_.current_bit_length - _base_offset_) <= 112, \
            'Bad serialization of reg.udral.service.actuator.common.Status.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Status_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "motor_temperature"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.unit.temperature.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "controller_temperature"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.temperature.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "error_count"
        _f2_ = _des_.fetch_aligned_u32()
        # Temporary _f3_ holds the value of "fault_flags"
        _des_.pad_to_alignment(8)
        _f3_ = reg.udral.service.actuator.common.FaultFlags_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Status_0_1(
            motor_temperature=_f0_,
            controller_temperature=_f1_,
            error_count=_f2_,
            fault_flags=_f3_)
        _des_.pad_to_alignment(8)
        assert 112 <= (_des_.consumed_bit_length - _base_offset_) <= 112, \
            'Bad deserialization of reg.udral.service.actuator.common.Status.0.1'
        assert isinstance(self, Status_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'motor_temperature=%s' % self.motor_temperature,
            'controller_temperature=%s' % self.controller_temperature,
            'error_count=%s' % self.error_count,
            'fault_flags=%s' % self.fault_flags,
        ])
        return f'reg.udral.service.actuator.common.Status.0.1({_o_0_})'

    _EXTENT_BYTES_ = 63

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8U50gH0{`t;&2Jn@6}R(YPwZrqD7#^SLn;!=I>KqkiS2cE5gRAjEY>7W6erONvGmq-*GyH?-PKf8k3ErAut*CVZ6gBPAP$HF'
        ';($0H4%|5)@pa>d#NUC$k>Bf{FV9TaWRc*4rIEX<-uL^}d$0Oi2Y&RA7pKa<{8ZWrZ5VmJ6-Mz$J>rc>cz&ScR9odlksrAxA{FB?'
        'yxU1d@o{nX{o=i1A)oP8k_c1Csr<;cGg;s=BleOU^b;OK#DWnmFAEKiJg8}_KzJPF+-c)MQ>+tj+i{oKBCq*vVXV>#$(_C5eg3$p'
        'Pt~WtQ@mf~^FDXZs7B_5E#85Wr+Cn(D)NKZm59QDS#y5K9rqpCDrc)jIhUW#cst;UXO)*F%6U%2sW6<}^0osWark;zzEGd8Pmv|^'
        '_&bGssmuNH)67T>#ZI+h#-Zzx=5B9<=KY3pek78XlSQ4uw18XZ$2x>*r}LAyd+fyKUB%u_+M;-TP~0i<7k%q^5^@s`3;GapV%~xi'
        'SxAbT2H{2=DZbac&ybP7a&hJSh4l*;SJu`puCHELUthhnzP$YE`IY7Mi!19ZtIKPbF08JsoG(aM)<BGA9*U@~k|ICghdL<oDJ=8+'
        '#86KBMyJa9dxcz)rz~6yMQTLAfuQ1X{(|3ByCU>cZJe*dVk<xHTb-FeU?UQK%HcphOaCI(fbqA1!`<7o`Y{4Fy#(D-6RP&5s>tWA'
        'c2dcsYa-S~{`oX(L@MwBw=5!kgG9sinJT|vv|v0yIR>1DvRvdxt2}$l-g%F*SvU&v314yx!;DCr-vw~-Sgy)7grN~Z^qF4r2T1^-'
        '8+|YG!&j8MQNC~EwF`rMzpv9GXHOGiJ8?t9FIaLDegayQz+0u++6<q_Kq>%TZs$jD^DtCNYm7*~O}krJ1UEaQyO7Z4Q6`G-7YlXv'
        '#5Qmo(@IcLuVoFm8zcF^DIWMPJ<JkT5o~bRYs5D7!~%U{H|0rrbhomGZIswK9&70GhXYPA#9sdt$<KoBWS|pgbQFnE;{0pdJWeAK'
        'vY~bBvCSrnv&boIvC;v{kSxaATt##Y7nu=ZR>Gbs%M{6ok<2oV=R(m`i3q)7k0qz`6Zhaj3p<;M6D?u(oLqUP&g3idi*oV9(z$tI'
        '44eyemN>HXqs=5Rr4m@HlRz-o%XAQA1~5VaWOoFT%baG9gwbqAiiEwn_14B)Z(j4}?n=SLE)FUyjZ>xNx(O=o7{X&6j<zE=6ILpo'
        '=vFF{5U(SS4GP}kCzs{x9C5uK@s_P>U$+WV?OWIrtobWiM}jA#L7J|D^tcRCO{2J@2!<4)6>^eZ$adbq7TdnH!Qczb5(#COyl#j{'
        '?=UCJ-4R#5Jz33cTStz!O2nMq&eAmMu<p`87xa7z(a(b6r?CDTSf9B&c>hl=thK=tDAysu7b(WPVRZzwu-*<K$&Cg7xwOp1B9J^$'
        'D3_#Xt)EL2*hD)R&O(E>m9Q`q1ai&>9IT0RNnQ1sR2^!oMui2^v_zVQMD;gWB;X%TO&~;QpU;~kNKI3<vVoc}TpeDaAjQgB)IrLM'
        'N>F4}_-wKdchlbO>8tsd$O9w3fht9{p}Wm!oAglhEHI1qh}}k~^rU|*N#%+BaJRbeoog_Jd~Wg(($;9SdF?*_4WCb#I%8p@Tzggw'
        'AJnkMlmXh(iRb~T0?-1|9cpvVrXo;H6`Un&g?yFdd?3FmKa$^-Kak&(KbAj~Kb1d`KbJp~zm&g_zm~s}zm>m{zn8zu<fX^*wJrI&'
        '{PKc)Ltd5}@`}8g??*+z7+01m%m%#{oY#7BLFcLp7Fy(>WTA;K58Ak_qh-H+Z+dEK13||z40=^H6b^tyw421rn#7AFhX9zPl&3}`'
        'jIkv`a1GMZHG~M-Dip?>+Zd8T*`yL*mUbc!G-|(1brP0Rxxtv^&=q=^RSpciiLjQ%fQZn>I9mXa&oXXVw^Q}hSMh#*&I-Y#bE$o8'
        'X-OpBj(Vt45i0I!(^{gprEN&{`%-<93R^9XEa^Z6a5z2~E*T|t$o9oOZc4!;Cz+Kxi$c~t=3BRJZf<Sd@CtcD-l|}AN8alX8(-}|'
        '-5VM}Uc&LBfiRgk$>fKsK?aSICj3v3_P0vu-~Uhf-=X|^wa;nTo5qYNgZeazLx@Tt@M~gEVdxv96PAeffoR`=sK-09JehYti1v^3'
        'jx0~+JpiHu<GdrwlX(w<=-@c-$ns>~84%5k^NuV}=A8x6>^Sep@?_o`h-%}!Bg>O{4}s{=IPb{vFz-yC_b7;tj`NNzPu6=3M8}4C'
        'YuWg6_cAeG)>*$<jizP$>b9B(@}!LALzzkaK%&~qoylEA{z3jx{z?8>{sq^*^6SH-esPNWMYgLVh5J&!4>Mabph+~fiK`i*yn9-S'
        '@{DTA84YfzYG{tOlLXS}L}xbYEV9gIJi<f@s%7?-N8a3~E9VPs9aa@C44B%{i=YKHyp>>G1vKf0klAXLts^t3wz&DsZBl0ew-Iec'
        '*RAS}F1#eO>WQT&sALb((=0W-o*Q<N;m!`7Wtneg)%@vL%sW)tjYuONh;VL4q3okbpCbvZ?C<4pQGQc+p348fs8{#<Ktcn<uaB?$'
        '73wZy_3}7kN0x^X%le3Y7ew!lBX(r@uN85M)pVSA?{WoiIgi`cvFes}5?I!9=ToEm!2^)>0sSDx8*c4l7dUgp&3{hkC;hPdh0pkC'
        '@gdz$%1>iv&sFzqeVRT4RTtig86VEXXuS5c|IggvNlV<p1=Xpiead)PePMWGq~p|{lo1N+Q&PZqid+A?Lm9v-)=2fum-mhD60`R&'
        'BsJbv02KfL'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

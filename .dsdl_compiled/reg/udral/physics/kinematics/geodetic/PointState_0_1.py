# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/PointState.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.279660 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.geodetic.PointState
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.geodetic
import uavcan.si.unit.velocity


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointState_0_1:
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
                 position: None | reg.udral.physics.kinematics.geodetic.Point_0_1 = None,
                 velocity: None | uavcan.si.unit.velocity.Vector3_1_0 = None) -> None:
        """
        reg.udral.physics.kinematics.geodetic.PointState.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param position: reg.udral.physics.kinematics.geodetic.Point.0.1 position
        :param velocity: uavcan.si.unit.velocity.Vector3.1.0 velocity
        """
        self._position: reg.udral.physics.kinematics.geodetic.Point_0_1
        self._velocity: uavcan.si.unit.velocity.Vector3_1_0

        if position is None:
            self.position = reg.udral.physics.kinematics.geodetic.Point_0_1()
        elif isinstance(position, reg.udral.physics.kinematics.geodetic.Point_0_1):
            self.position = position
        else:
            raise ValueError(f'position: expected reg.udral.physics.kinematics.geodetic.Point_0_1 '
                             f'got {type(position).__name__}')

        if velocity is None:
            self.velocity = uavcan.si.unit.velocity.Vector3_1_0()
        elif isinstance(velocity, uavcan.si.unit.velocity.Vector3_1_0):
            self.velocity = velocity
        else:
            raise ValueError(f'velocity: expected uavcan.si.unit.velocity.Vector3_1_0 '
                             f'got {type(velocity).__name__}')

    @property
    def position(self) -> reg.udral.physics.kinematics.geodetic.Point_0_1:
        """
        reg.udral.physics.kinematics.geodetic.Point.0.1 position
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._position

    @position.setter
    def position(self, x: reg.udral.physics.kinematics.geodetic.Point_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.geodetic.Point_0_1):
            self._position = x
        else:
            raise ValueError(f'position: expected reg.udral.physics.kinematics.geodetic.Point_0_1 got {type(x).__name__}')

    @property
    def velocity(self) -> uavcan.si.unit.velocity.Vector3_1_0:
        """
        uavcan.si.unit.velocity.Vector3.1.0 velocity
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._velocity

    @velocity.setter
    def velocity(self, x: uavcan.si.unit.velocity.Vector3_1_0) -> None:
        if isinstance(x, uavcan.si.unit.velocity.Vector3_1_0):
            self._velocity = x
        else:
            raise ValueError(f'velocity: expected uavcan.si.unit.velocity.Vector3_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.position._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.velocity._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 288 <= (_ser_.current_bit_length - _base_offset_) <= 288, \
            'Bad serialization of reg.udral.physics.kinematics.geodetic.PointState.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PointState_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "position"
        _des_.pad_to_alignment(8)
        _f0_ = reg.udral.physics.kinematics.geodetic.Point_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "velocity"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.velocity.Vector3_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PointState_0_1(
            position=_f0_,
            velocity=_f1_)
        _des_.pad_to_alignment(8)
        assert 288 <= (_des_.consumed_bit_length - _base_offset_) <= 288, \
            'Bad deserialization of reg.udral.physics.kinematics.geodetic.PointState.0.1'
        assert isinstance(self, PointState_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'position=%s' % self.position,
            'velocity=%s' % self.velocity,
        ])
        return f'reg.udral.physics.kinematics.geodetic.PointState.0.1({_o_0_})'

    _EXTENT_BYTES_ = 36

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{`urU2ogg8OLSGmStOU9NS6VBu$t!O`OD4D85KkyO(U~vSMt~py}FdT_I8ulfy(3HIj1ebOqRp4Jkli1j+&Z0t5OH'
        'da2zN`vgTXpxt&;>~6p=db#I_|6?ag+@ct;n>s-99Fm9Ujr{%25l^D&KRtaeH~tf!9Bg-jPPftw9N)FO?tQz}bt=ua*Bf|&8#-xx'
        ';AZF#+u_i6Uf&)#>4)k0_tW>%^?0V)w|jJ5_MJPGVaK<-l>yrh+;&j8=k}eR9rENI$Llzhs@(A0et0vqd6A{&rsD^$*H2k4o_z!9'
        '4^uN|PW>T$KaCffb{P6@YZy8~`ZiUzM>BVFrSZ&F*Xee4n>XL=*rDAFd7D{2JIQ9^i{GKODVt?;qD`z!?O;nNXl1V!4ScufhVCY{'
        'Xzps)v%^ORZK2t6!)Dj%-w9c2UZz&I?I3LSsM?erkB{6CxAWU7SLoU`eu)pw@6*@Pc(oaXcE4l$orep0K;`u8JAF4Cc6i0NeY+jf'
        'kOnl=SCOVNZs}9GT(#b)*BWY7)r^{=R`t4UR5e|xYl>P|t94mZ^;*4Q$aR^buIPrQH5xU&VKl0BtzI)^eveX<>xL{VhOQd*nyecQ'
        'T{mi~Qm@sFx>2oHbxqdzSyiuUs-b8#Dqd5Ss;blsqd|vNgEAW$RY8AcRafhJwbn3dGSya<^?FU$tBRq>^_rsTT0@o_vT8I`g>Kg5'
        'I#p)qvY}BXRc%n&yf#%)Ym`e-l!j(hYq}vDy53N!Rz;=WQWvS~hEh{xt*U8t>O3`8rPkJ~hTNz&lt#las){aC+hwIzHMFXt8B}h~'
        'NcrFoTlD^vy7Z=G!#v&Wcx@Wtw|u+f+WohAhMo6=oj~f8d6}JNXW6+2Y@J=)e+2*gBbe)Y{X5w+VDetWze~I{v^U#!zY@5WArVr^'
        'n5n$!cAT4SyKDOy=2K=)V7~tp{|`@brssr?&!1q9PT29vL&|TqwzJ9Qy_EfeT?t5=9cSP>ZJIqg=?C#*^R~O?beaRt51Vc$y&fNG'
        '2HwzbJ9MGzGzT_GF`nh2>$XUUH)t-~y1~zWND`j9MDQ|?PhQ24qD`JG&>NM;^H;V9%<jJA^t?1aHW;?LZo5e{#<0t4-knkChGO<w'
        'rExxRsW|>>(Mbq7UfF%UD%FZy;ZsE#a)YllnH^9IeWxGtxnt99JLv~ZW+n-x)uocpikW5C@RTu}JWk{CPu=j9@$pSM#2gbBn%*Fd'
        'rM(IXwtFp)x<xIyM%|=&i_Z?P4jkVOJ%4wmDmL59r3sa}@xdE*r{nhTJeG;|`PJ*gE_HKz@+y_EX?KTC`p0zLyqp9rn)U}-L8)09'
        'wy3*3x6da*O4wUGG0P`H8f#v*ImPeGC1xJ6z~fY6PUCon$LYi@BF^G^3D@UvJdf)OJkBL%8OH~BEGOn7kEO&si1SOh{}7J{5_6fy'
        '`NUk|aW*kmk?%0dKf>c`Vm`&=a$>IWxRjVr^SGFpM^Vo)lye;QJ;P%$F;AeplRV}VQ$qcxcs!Yyr+GY)n9uU~Ok$ql@pxiB$K$cY'
        'Jj>(J#5~92(}}sx<62^#=kck;yujm;#JtGk;l$iPd!OfVB{3^#_az<=C8mt_S9v^`m<sx#VmvhTN9S=NF>B~o9ph`De+`V+3+U&I'
        'JkBKM576Hq@>odBAEDnr#&}*v|6k7D8}k+-L)=1qfcO#O$B3UGev0@R;#Y`YXYpET3W+t5SQiOHBwiMYTOz?kVoM|*h{Q)C@v%sJ'
        'A`+j9#AhP$l}LPz#E{l-&ep*0kJrLD*9uzMs>AMvJ2PJRlFJu?ZAWT3;X97gmqO-9U5{)d^&Gn|1&%FsolU1JtzWzO%6W+vjN>e~'
        '$5{q^X)AfR$EWOm==A$`MdF6!>rP43B-t&G4tXXjq(Y8%*ejg*OYA6XFope%y*OmoKVYw3XE)f*b@n>@C3}Ot$!@V<#RYOEEy>60'
        'Y%bz#rA>a_U2D_ANvyWhcyYYmCQnv(P04JsV*Hn%Ba<}#Jwjvif+Ut;8`927U}M}#(e}#x>(p$|?>N5X22z`O0Usq#qN>|0>-ZL3'
        '80R1#iP5<JvzH`VJNHmP;NEw}<#z3DZ-_CY+XC@}h!^hsc1VLtW%B~A*gj2Pv>M^9rNQHi_>{GnGd3b)?B0$z2Ro^I56SfK6|c`{'
        'x&9Na9M5G^rn!UvD*Bev{+(6&pS^O1+4XmXpV_uKMQ_`ETI#$@e}A_x;e82z-z3aF7v_Bo4=3PkM8rn)4Q%8m*eHOFJlM!ju#pEF'
        'C9p9IHcDV)0c_;KMrneLIk1rj8;fA01UB+uV;O8502?K+Q2-ljU}F_*EP;(O*eHRG=?ONT0UJlb##3Np6>J;=8;f9L0c@1O#thiV'
        'gN+MdV;yXq1si9;#%Zu2fsGSj<2cwj3O3fj#u2cw3O1I(#uC_A1RG_rF%LFMV50~&rol#jf(-*~tb>g;uu%dV5!i^pMg%q@un~cc'
        '2y8@PBNA*xf{jS95eYUT!A2z5hy)vvU?UQ2M1qY-un`G1BEd!^*oXuhkzgYdY($)mZN7ltr(vIleHw^^ZZ<WH2!_!&z>u4OArBaG'
        'fT1t}Ljf@40mBSn$N`3Vz%UOO$`dfm0ERMP$ODElU?>2FCBRSu3^~AX2r$e8h5}$%0}RW6p$r&`6EGYD3`YRNA;3@u46}eC4;an>'
        '1_>}62MlX~VHGee0fsVQC;^6Pz>otB&jW@FfZ-fqI0G0?0frNR;TT|80}O`&!!lqv2pGzMVGb}90YhN|1{p9c0ft+E;bp*J0ETtI'
        'um%`PfMEm}Mu1@i7)Anyk$_<&U>FG)MgoSBfMFzH7zr3g0)~-*VI*J}2^dBKhLM0_Bw!c`7)Any(Zf^2J`MXceD7%xpKrvsi<E!o'
        '-D98P<itM3rqlJ>Zn#}}!)b?}uYSWeMSN_J?NQ&ix6^p_D*sxZeJTD4KlSLI<bkHsb$a}BbhcT#yXPT2wC53@Q#DyJ6jiI$R6|z`'
        'LvI*WzRyuLRL#)%u7jd$nv75U{9A=Ruz3$sv+(3^Aa1<;nlo@h_sO52^UZtw)<?foNXd9m@0%70#`+F|nVJyH%!FWy5KIw*DNP7w'
        '27)O=FvSVMEI=?t2xba`S%P575KIYznVt~LVF+d!f;kAmlp&Zo2&M?Z6ea|70)jaX!5oEP)*zT85X>qBvkbv3K`@IDOc{cihhRz&'
        'Oc8>ahG6m&g1H32R3Mn=A(#ya<{|`h0fIRX!K_0t=OCD~5X^HB%ozygSqSDd1ak_4ksz2g2&M$VSP+Z_!B`NC1;JPlj0M415R3)E'
        'SP+aQ1Y-%oSVAzC5R4@RV+p}nLNJyPj3oqP3Bg!GFqROEB?My$!B|2tmJp031Y_+AW@)^c)+B<+0Bx_|foN?0$@Z>Q$mQ;SmCxmZ'
        'J-*knU$eK^Z{m_rP8u&kI*)E%jX%jU^IJY>-u;@Y+F1weW4e#&KBia)>;RVGneC|D{etsy=<Z)Rre9KeuWc3f1^bfyo&AITGhW&K'
        '?^I9PHTg5&zS!AokpiBNZ(rEi?$3r~2a-47dla2)>%tDR%Pp_7y}`FNI?kr&cKAu(3&)!glH0%S`Mq&^yg%YQbnI-5H$Fti_^rXf'
        'X}h;wD%#Dqrn1d$sqJ}w$L;f`WScDCVQ1vq_A>tU`0oz(`SoGzE~7ym|2)4YO|f_RKjM<O<FO0;VO9PMdwqkzBqsm>'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
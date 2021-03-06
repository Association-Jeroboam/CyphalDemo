# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/cartesian/PointStateVarTs.0.1.dsdl
#
# Generated at:  2022-05-18 08:58:48.097349 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.cartesian.PointStateVarTs
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
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PointStateVarTs_0_1:
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
                 value:     None | reg.udral.physics.kinematics.cartesian.PointStateVar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.cartesian.PointStateVarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.cartesian.PointStateVar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.cartesian.PointStateVar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.cartesian.PointStateVar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.cartesian.PointStateVar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.PointStateVar_0_1 '
                             f'got {type(value).__name__}')

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
    def value(self) -> reg.udral.physics.kinematics.cartesian.PointStateVar_0_1:
        """
        reg.udral.physics.kinematics.cartesian.PointStateVar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.cartesian.PointStateVar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.cartesian.PointStateVar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.cartesian.PointStateVar_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 536 <= (_ser_.current_bit_length - _base_offset_) <= 536, \
            'Bad serialization of reg.udral.physics.kinematics.cartesian.PointStateVarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PointStateVarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.cartesian.PointStateVar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PointStateVarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 536 <= (_des_.consumed_bit_length - _base_offset_) <= 536, \
            'Bad deserialization of reg.udral.physics.kinematics.cartesian.PointStateVarTs.0.1'
        assert isinstance(self, PointStateVarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.cartesian.PointStateVarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 67

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8NVSAw0{`utO^+K#ddE2=XNEJPq|xZbv?a?euU13Z8j5VbH8*kAioA-vZH)y>_738#$tGEvYKmlY`(-q<zy{ev0tsj!1l$4q'
        '1p@dR#JBJiILIQ|!!Dw{0XpQM>?sHW#0hf9Q_X*IIIWqrw3|y13K%}c?&_-Q>iRwZr>dIzgXEul@@_2r=f5`CZ9DC5uI@0~G`i*w'
        'jb@kS>Mg4`upHB6fq(RlYkMu%v)SF<0Si72F8?_AQIPfL>wTj~=PNeb%6V<u=;j7|*D+g8?!MV)J;N2rmSMZhF^zuiwq^F+JFelf'
        'j|}^+6Zon6HnSbm>IXdLFMfpdr-2^R=l&@8ao``R8?I}cO^-?lzE4#i(%4C^z@NWivTl2?k<0bA;Tm;Uw4BGs2l>2z!85j7)F#*L'
        'vD}^Aev8{y-~1tK-=zbNYxD*IU*t>roE{S`;c2R!ui)~NhqYs1n?2Jtx2YW`KkPf^R-d)s?YnG?+55ZhNWE#g^)BmgxjfJ{YGuoC'
        '+<MPyQ!CH;XKu@a#AUhbbnccoMO`!ZhrtJdf2vMx?6(cOJzdZvuSvIdq-VBl%V906-wym_y=}FE&0oZ0vAdipeXrMKwqo5=rgAxo'
        '%MDlI#x_$1hU2id;+XvwQyi<u6vL(}Y{TAFdi1sLDrTSZhdJHcvM3bCsZh%{x9D`%%(2{+Fqi0HrD-_qvSK<)o86<4(N+e`UN;7V'
        'uGykNV)b*1D5mAvwkT(EiKxkQ*fKpRrO6bV{lKGVLzmyPt=?Yg&gAihg(*F17_+Y^4r5`amPO?{1G-VOzePvwZIkXTY>FAyzD##P'
        'joUW59uuu}Ev3)4MK{sMy{`3O+`h^Aa%G*mM0sGgshzB4P#eFsysRkeiuy^pvcG33yV0~fS5Z~1tn4zwcCIK7xY^?3)PSCxyPH$4'
        'DV0)K=G3*+ZjZ)}tvs;2ZksBi8WhFr_gRZMj$xbK-Ek9WASkBmOj=9bMwd}*#S<x0tuD7bN8}2tr_*hZick!yjS6NvCiPd}rE#pZ'
        'Y|}BF-1ug$cWEq`t@Z2IHk54Na+MqJTvli#^r<gxs*lK~LE#NVe^r&{E<q}492mP@%Ltz_Jt*=Jxv=4P<)c!1qWN2t+2KaFE1s|z'
        'Zd+Zp9%dg`agXhFRFBbt@fdX{&w&QTnk$Bd=mT4v?bCx%s1u!BKp-6RQ`fD&z{H(!$4~O}NL|o1{yM*?#{^G&ZH&(1ha39F``_CL'
        '_+|gn?=stpRvnHvdTydO?)R++{aoNL)WZe^{;Sd{u$=)7IN{9pxrEdQ;rKMVvOT=)FVQWx#8Kf6Zy-(Q{keP~TIMvpCi72D`N4W~'
        'ckFk?U1a$yyvWx*awu&^l@d;@9X#@n)$f@*tX&rms&2M}4gW;lu{^uQ=tP&*2L`zde^HpO*$n)p+vMwaZi}Ozl6#uFN{)kD!nwx>'
        'X5cSh-yP7idWZF_z&|_ingnj0yuQ~J_3e3Bx`~CcW2NgwUj_d81D$KGkjv*pX9ccsXD932aHvrN|2hB-9??VitBo=6q6S6OAVv%E'
        'Z`tGxL??@JOHdmGtoy*S@2`hMI8$|o&n&EzMvBY#5k>`AU2p6ILKm=C4}Ib07AMB2SFIj7xHc*l<F#o~N#vcR7Y-TRraYFt?hIJV'
        'yk}00a}tRAEGK+%vrAocNsf~}*G)I=M!yGs`nOH@z3}@THW|czqHYZWUpcH0XSdh1==o5u-lFFPr}#e6Xt<WWCqWDK7AO1z{(JuM'
        '+eTaX#%D5dL!904x?OVr(X+h#$3a%thE9`&d@wE{&{JNM?z3n1g{)D+*b#|EA#F5TM4|eexGpx-<FE-~<3l}(@AJaW4fO>aU&Qeg'
        '>=KSI3%fAXk05_q*wj!zDr|D7A4C4*!X6pwD>#2b*!iKpigHd0yE@cQ3A-}XPYZi&sGkuwJ=9+kc6q30aQ(}u_Z8H07Ui5neXk08'
        'cBr2h_LZUjny@bqbw$|BP`@DTOGEv2Vb2WpZwPyOs9zNJ)KLGXuqTK5CA4cz*b_rNi}qa>_V`eL1MPfM*rP-J3fjAl`^}-<SA|^~'
        '>Up%kAnf8$S8*Rj^hXKz6F%3(P_N*=s_0)0_g5P~cl}$izXAK3uy4Ws7VNiS--f*jy9vu-cVHjFeg^wF>=&?K!ajz53j5XA-b&3O'
        'k&%h4OlUH3QzkZLg3H8?Ogxl{&t&3rnfO8`zLbf_GVxR<zCyyI=#CVDbVRsz9BT^4PKvYS?!}vz{g@E0Nt8Jiu9kk45PKZKB9@Ls'
        'uv2AUeUY-Czt}4;QtUHj9$2Id+8s0JQRtQ%yS?1^$mM^;TI8CF&jjsLG5gs=<_@-P>{3L1LkQ;B+g=lg_6O`o>#WN}l#7|fIe+N}'
        'MLF)iTohEiO+kgq*B;U{?-^UvNKZucZ*7+6VzENCR;|>Eg<?sosKr9Ln%4@YvRW;v#cHuo&6kShO0}ltt9i0zwXBs&wOXZI(`tok'
        'sanzU;u^J*uWI=`1(QXsTFIBSTDh!MifXk|(W+XZS}2$DC2_P^E|iLzTB=a-rJ`CWsufME(bs}TnY9vCL4WyTxmYb1DmAT=r`ihn'
        'a<x(}7gSBnS1W3%T&m^swR};l6;-;pl&?}{S~;(kC{wXmqq0S9MYUL=T&k+pN?M^(*791pTq{zoYLV`iZjo+XQ!8q|R4A3Ibo12M'
        'BDJ<!(DJoHO|8{5t)Q0k)b_kuDQKmFTGFW8iWWveq$x`@LmC(@)7=g91pkn4jy33G{>hY7t$x4;%ry@dym<Y-xYXcVQ}XrpFa)uy'
        'k9d#%`iJUMETT_w=u-^(l!)k40{Rq(KFvd)V$i2$=+iRvDGhy!Mf52ReTqY$($J>_^l1h9l!89Rpid{DPs`A!1oSBbeOiS+rJ+v?'
        '(5D#m>1;%wPC%d1(5FS{Qyltq5&EP+pUy#_GSH_}(5DsXQyTh|f<7goPci7zI`ruc=+heX=_2&$0`%!T^yw`0DFb~v4SiaLJ{^ZX'
        'rJ+wt(5D6HQv&)FgFfY<Pb<);P3Y6jh(2YZPZ{V_3i>pHK8>JHBk0pe>eEQ-(@5&mNb1u_>eEQ-(@5&mNb1u_>eEQ-(@5&mNb1u_'
        '>eEQ-(@5&mNb1vQ=<%N*Aw_Av$7ljcg2eyEYa0C8kAlv9@?ZR49e({0e`kY#hu_Tdclmd@&fnv=_=X>MXqJ!^PMKx^SdH*cO*!WM'
        '0YAU<NECiB#x0rZBt)h6MMyaVbOz`Q&^<uMD-P3u{;go;>A`^d35vx6e?E-H#I%1LkI}q-FCq*4rAbT{_{YMijF2rvp!MIlE^{d@'
        '%d%<GXJFmOPzK_na9T`CO%vX)<J+6@J>z@E_t)?}H5K}Ir2d2d=VZpQf*A+@Z~m4)Pr-Y>gqXP#Bfj*711an*(7ExK&eAyB{=j%e'
        '2F4BIvhf03&PBMKk8rsVS-43>xSR)<X>hp^;qnN$TmYAIk%gNyxJ-e|WQ5Dp;BpmQ9tW3caJd977r<pA!sU5zc@A8@0xmP)@(j2<'
        '1uj=33pdBWWg1*AgUb}STmY9za2bzqc@<pdz~wr)yaF!Y1eb4s%gf+03oh5d<t1?WO>lV;Tz&&wz78%gfJ+5jX24|%TsFXE16(%1'
        'WdmF`z-0qmHo#>ATsFXELvq=WTs9<^4asFga@mkvHYAq~$z?-w*^pc|B$o}zWkYh=kX$w-mkr5fLvq>J<MLR`+BR&`z80%{wkwuw'
        'Y9EKe@+a!|73IT$*w?bnE$%9=$hOsGLK(-KQ1VKJ1lKlq#3lt3(w*(xh?5RJ>HHa)&hOBNcc6-Q{*E~9{Jr@22l4Tb;^Uv_!#^RH'
        'W)2YSuZ^<zO`uO-xB6lap?~0_v6zI5HDjCg#cu3@n*PsYO`n@-`b^Vjnl3cG^8q2v9OB`YGRJ%3<N1k5M2MJ+5D^0rDG(8l5D^Cv'
        'DG-r}5U~OxVjv;`B2pmYIEaXYh;)RAqaY#<B33~}DzXi-3L=&wL}Wn33W!L7h!}`?6-1l?5ywG93Pj9-h>IZNJc!7Eh*c1g1`!Jp'
        'BHjcMmq5e?5OEGfyaXavLBvrIkpdBk$Tmm`MC3ul6%dgH5f>wB8Uqm-5OEts<Uzy=h<FGhc0dFN5t|_5W@H;AD~ZTRB2plN#vhOf'
        'Q#U86%}I(+Qah8>!%6D1N$T@S>WfM0%Sr0-B=vNX`bwt8e1xf{oC419nBg(Q;~6{<d#1wI@xqtoqSL~?9kTK--E<3Itm%&5xcZ27'
        'EwP(YoZ8Wg|MDHZ*CN|*+bAOU^_y=8&Rmu0nd@4ylvg#iSgKTtT3OY!a!o6UO|gPjENLaNMWvQYrTo6RZQ}Xnw$V)=Wj42+&249M'
        '+x>Ifm2e(grzu|@?~YC{FL#nO+5E3WEOyuyP^TxRqkS<QO-aWP_$$B8_RoBBYI%5u>I~Hxs<Y+c8J9CI{|_w>U;8*4>gv_8rd}57'
        '#J}n?@y~<?{~Kv==R5QC@$=-1tQ7l4rlSAAKRq4)lQyf-ecm6uNAm{5R-~4XU!LA;UT*pQrg&4E$(Q5J@oyaz2R{}vx{Bj9!*{9a'
        '-VU2O+-VtIYJdn2g6CeS?)*g@-l_AKlsarF+D=X_MbG@y%uoHl_fwrGNi0Rrwq|BqGqbIk*~>>W8fG*^UOw7ez8Oz25q<s(1)ltI'
        'XM2GH%3ma2{3V4m`+l2p(5r=K?=Yt9<qCgn*JiF^cAfwI;PB7mdy7l6ji=eh(`@7EnT@B;`}6X}g(m`#Cocj>ECNXK5QU5Zki`ff'
        'X#kQ0Ah8G_$%sPE1CSU1Sp^`g0OV8zka+--1|X*aND_do0FW2}IUWII6@VlG$jcFhya+%t03;1SVgTe-0I~`|76C{WfSd;)rvS)u'
        '1dufVavp%31|aFk?>F-RBnv<k0FnV9D*z+~Kw<!-3_x-KWGw=SRLCp<c^iPl0LV=Mk^vw?05Sj|w*g2VfUE$JrxK9I5|A&YLVh6?'
        '@^h(>pGk#$C>3%?DkPT*xhWO$<}<(F%u0pKNQF#ED4tB9crt<F$-b8rW=PDCm?1HD$gadVXykv*Pjvotks__1zG%3ZiTrOtzuv2@'
        '&leQ(`eZ_=(S%SFZ1bONkP`m>f>gpxoUo@4d1~Shq9;VJ<o*Y27)B6jNdN!'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

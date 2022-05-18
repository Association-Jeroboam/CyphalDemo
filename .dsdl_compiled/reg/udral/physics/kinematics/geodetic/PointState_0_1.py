# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/geodetic/PointState.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:35.920818 UTC
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


def _restore_constant_(encoded_string: str) -> object:
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

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8$FPKA0{`urU2ogg8OLSGFS4yTeoN{mX~Lvw;v}v@@kOHAy<|(56=RbIP1j~C3Xzf+AG(sLk(6g=D8OE9NC5&PP!8x97|@T<'
        'OYN@v1}z4(+iup~4cNtcx#x)gV<$@7q8PB7IzaLql85Jw{Qb@mPol{`%wEim{={ecyX~OeDK`SgckPaQ-)?rCa--#S`(EINP8uJ%'
        '6Z(TzIPjg<cl%EIL3-)E^xbqlo@(^$E?t*>XR|zL`*x??XS;#h3d--eJ*R7jJh|z3ZHH3j+n(DC?}Rolve?*m{J`~kDa*w(Zy^0a'
        'YUa#|-=*)R@qEJ$L*H!<LMKSyrpgXz=3cHep1R>Wo%Vk7<{E7~v>PFBGs|Zu*;IVxTeLQ1Gi+A0iIu1wY!L;m9Mqz|?{?kL-KG}J'
        '-spIC_~@X`H=1tP=s3O2kfr7|YGum~!bX>>P1&jV_-%1JzpZ?ouHEF9_|W_|eJzbw8$oFI+P2?*xS$7APS@V-x#6JAE57I3t&oN^'
        'prO8jG?j5zpUCAZwR){uS1YP!R28+N*JPuj=}Jvg)S6nU$(pKHYjs1e$rN=(H#DtYuj+N9Ua4udsv+}xl&V}aWLYtE)u>fv-Kguj'
        'QB{>%wQAIiO0A-6vc}J<dPP$WMXOTrnyOS(rD_;;I;<F!+0dv8`YWrtTGK1lx>1#>wu-FRs=8iL3`MS06;0RbvRs!{qpm7+vnJQ5'
        'GDDXQjWVffoyz95sft>qT#BO9HKS714cXB3x=OVwD)pASNL@FSsv>I@O{-Dosj(`xwpKCZdZn(^>xNNLbeY;NE7gjjRTRyja;rwl'
        '2Y=9{_ovvQHzgb9$wu32(Fnig+ilnGz0EW1y&vo}QfJL;>>RtmE<RxE?8@OI_}?GFY{%<uX3v1h2Mzx|@zTKFZrQzZ;FbqONI7Gs'
        '{HEJ>?zHTV?Pr)zm^p#@;ZyuSJjJQ56FNSBf;l>2$14vhztP;yCYN_p_A_=pAZ@mtzVEbX_GqW?#|w>n?vB%L^gTapxb5^-ywnK1'
        'f!}iILdR+JZIWU<!$Zeyk`QmxT()zYpZ$O&JaLuaWgefr@_jdr=dSPencaEG>3V5=vOj2c+*X6;i9v_gw?B`NPN%b%iEa$&#!3D{'
        '(Mf1HUfF-C%9XNQ<`YC3a&NCRm>p2Ne5V)k8DraRIqCaMW+rK**`bmzi1}pS>y$AZKThM)kKOQ<(eWKR#LN;G8eTt*rGp9ycDqfF'
        'x<xIyN!_H`iq8qJ_8s32J%4|Gnr^h1OVcQ0@zL9MyY2QiAIrqL{OYYihq}2tew9ktwmSnS{e8M_UQ2=|P4@k)pwui5n$+E{+v8Io'
        'CF~uZnBmhOjWsXZoZ$E65;Koj;Bg``CviN*<78q^BhKJ@5!YvNJcsM^JkBO&3CBlxEG6awkHy41it~%Oe~HH<iMh<<Tw<>9IFp#G'
        '$af6oALns3F`wdbIWgCGTujWTd0a@$6R77T$~lGlp5bviF;AnsGd$)KQ$qb`c|4Pt=XgAwn9uU~Ok$qr@l;|y$K%Pwyujm$#JtGk'
        '(}}sx<62@~;_<1(yv*bA#Js}evBca!d!OfVB{9or_f;O35>rO|D?A=eOa=W=F&-NFqw_eQm{s(vhVeDfzdFY21@!Yp9;XuXd+6`?'
        'c`PL6576%)Vmz;*|1W3njd>T5A?_ePK>QH#BgBspKSBHy@k_+7vUsyNfyA0ftc!#p5-*FyU6EiSu_F=>MB+n{_(&u^7Ku+p;!~0M'
        'QY5}YVn8c5XQyxXMk`>PYX;41tzmb<y?HKt$>mGGmLoNt@YjyhlS1Z59gl1ybsf7W1&%FsoNcEgt>3)!$|Z@GiK8s{Mp^oNK`VLp'
        'MyKpv==6GaS>j&gt4&GNB-u@m4tXXjq)cXZ*ejg*tLy};Gll(yy*OaE-e<4gVz=3yb@n>@IeUY>$?nDlGA1p<M{8>?-)wbFcHLiJ'
        '(_%@iu+w;9w8kb&R`xx~EOKJ}r=KE|H2MufBlChJmR%dt-t50I>Y`|QdG2*;wCA@SUvdMf#k_!zktb2rEtYkAhc1kAkd4Gx-1^B&'
        '60MiJC?Ig}JEL+t_O3U;h|z6<_z}blcYZaXA*Hf;0oQGxrYu^4@Yd4M@r8TJY}Ow6kZrQ9J#Bh>sjY`pdhEK_<1<_DiB67ZGbPi^'
        '!G8&TLuvoYD*g9CIfLx_wy-nXF(>F<+ok2refs;GLj@ly_`9ZH_L=bRV|X|LXCopuqOV~iKgLD@Y~;a4evFMg*eHUH8L&|V8}ncz'
        '4>pQpY|Mg<JlI$O8%3~@2OG;^;|SO&f{g;$SOXiYU}F(%l)y$2Y)p=^@eJ5F0XCij8>?Vr32ZEYjd`$91RGOeBM&w%gN=2taRF?c'
        '2OH<Wh6FZFgN;*Q;{@1P0~^P|#wyrY1{;fDV*zZGz{VWdD1wb?urUcX@?&fmU}GI@tbvUp*oeSJ1U4eD5rK^eY(!uq0vnNFBNA*x'
        'f{jS95eYUT!A2z5hy)vvU?UQ2M1qY-un`G1BEd!^*oXuhkzga@Z0zvm`yma7G#t`E9K4fF4MT!q_%$%(#$d<;h8$ohjKNR<40*sX'
        '1sHOGVGc0N0fy2T3{!xi1Q_ywp#&HTfMF3Z6ahmHFf0LvIlxc=3~PX488DOp!}J&oCjrB8z_0`uN`PSoFysNldB7k6hEsrH4KS<%'
        'hDE?o0t`jKFbNoPfZ=(-a2YUM1Ptc^!&$&^8Zev$3~PYl7+_ci3`YS&2{6n8hH1c17=u9u42yu_E?{^WFc^Sg9Wbl`h9Y1X0)`=A'
        '7y^c&fMF<L7z!AM0*0Z0VJKi23K)h0hM|CAC}0>07={9dp@3m1U>FJ*h60A6fMNLX)Nn|{Ar0So8pOvN@$DkzUwIGMn>aJJH?i$>'
        'yp|j8mfvt%q35e#vo#T)JYY-I_wC&@UcJG;kZ0eCf5cBcx(|7z;dGoX{}`QZknZnuNDu9E#1~afRt!bes#Vp{6~oZ$MuqQfR18%!'
        'G``cI=$a<uvp)Y;VfSs`gVZcM`5Op}mtS-GPUt@Q19ZOe4!`x$FBMWU8q{6WBEeYSLNF6!f|(i<%rpcu4Z#%01TzJ}lpvVtF~Q73'
        'Fw+ps1O&4P!IU7FA_OxzCYWOo%rXRX6oM&1FtZTMGz3!^6U=D{<`e{T0)knCV2(pDs}RgG1hWXiEI=?N2xbm~DMB#Q5X>Y5lOGez'
        'RS2dG!8{MaY(OwqAehS#%q0kB9fG+C!CZh~o`Yb{Lom-mFy|ncvk;5~!K^_rMF_@%U@Qp6f?zBN#)4oh2*!e7EC|MeU@RdRO9;ji'
        'g0X~PEFl<62*whEv4mhOAs9;t#u9?DgkUTo7)uDo5`wXWU@RdRYhN&nqYbnM5kv-PdA&A7WAhKTTa7|4xAl*FE*CuUYc2Z)`z3oT'
        'E(+nK@gkJ-=*HFPgDf+@;dAEJf2g9pRlp&nhmamZidDcKU>Tg*Zpzl@oR_7oKXXXGp!AcsRM_Y23-(v`H}>~<W&giVJ!!|}k9_N5'
        'Z=Xd9cs{;$VQ2e38<HJJUZ3wzw6kpsJIpROz4q<~-_mG1+n(FzCw(s*ZA3_J@1Ey(N9obti0{y`voYHA5Z&Up27RaH-gBvFH`|oT'
        'wz;L2=lN~7$D5LEuzZVMk#E|^_~+xlIoM~n2F<Na8q(2E^PAEHyU+g-m&6^9UEq(Z{9jp9!G07c000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

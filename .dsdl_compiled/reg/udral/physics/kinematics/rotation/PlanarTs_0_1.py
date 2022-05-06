# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/rotation/PlanarTs.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.273728 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.rotation.PlanarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.kinematics.rotation
import uavcan.time


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PlanarTs_0_1:
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
                 value:     None | reg.udral.physics.kinematics.rotation.Planar_0_1 = None) -> None:
        """
        reg.udral.physics.kinematics.rotation.PlanarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.kinematics.rotation.Planar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.kinematics.rotation.Planar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.kinematics.rotation.Planar_0_1()
        elif isinstance(value, reg.udral.physics.kinematics.rotation.Planar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.rotation.Planar_0_1 '
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
    def value(self) -> reg.udral.physics.kinematics.rotation.Planar_0_1:
        """
        reg.udral.physics.kinematics.rotation.Planar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.kinematics.rotation.Planar_0_1) -> None:
        if isinstance(x, reg.udral.physics.kinematics.rotation.Planar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.kinematics.rotation.Planar_0_1 got {type(x).__name__}')

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
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of reg.udral.physics.kinematics.rotation.PlanarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PlanarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.kinematics.rotation.Planar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PlanarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of reg.udral.physics.kinematics.rotation.PlanarTs.0.1'
        assert isinstance(self, PlanarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.kinematics.rotation.PlanarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{^{OYi}J#89q+pYp$+yYi^yCHnEGnjjuUrNt@shrA*^QiCY4qY-V@IXU5qZGrP7=B_#R*lt?Rer7Ti@LVrSkLM4P+'
        'zLk$iNK_yYUy%9*#QW~fo^u@M5EZFJ%0BOznSJl`%&dR8=Qjr@8s)$2rMT^B&$n#Nm1MsBkU2iLY&QzxNXvv5+5WqUO5G$?e6=0('
        ';&CzcQSpmnG8?o*7Qnovc*{yX#e6FkZ7p4GJ&+*}Sc0O85)h)$y6v-&sa0KMBlZSY8paCI$cEoH^5cRw=)kXwkBV%s&5}e(Cr!96'
        'J^)jFob0SBvcc<;`(D?%G23GavlH}K?5YOEV0JcT8!ij2L<Zct+YVi!qELRwy;T^{2@B#v42w}ZKpW_Z*az0dA@lk~KR;q61DVJT'
        '@MGe=P|H@xy?4Tdx47D#vc0w=6WixuD-i{4f|oASi5)~9czG&2db?JHuUX45cN3=|H3PpY?iAT!8+;5sro3K7k5UIh+Z#w%MVh-&'
        '=oQ%>+l$=d-d}b#8moenFby28NVG<JR%wz5mJq=<IEk6o+#_0sE+;w)IAID*D5lyZfS+MPWC-iam5DWmO3gSZjg)M`^rW=7HC?X4'
        '1QUm8K1HM^9$$lw@JP(n42xr5x>ZjQRO6;fp`OkwXerfv3<^aYP89!n3bldP*HjdAwd+p#N@XMf$GDm%n)7mz8-ZROL!dHj!Km7h'
        '5L@YrEUk}06yV$j^HYvqCJ_nw2BrxfYkss@`PZ3WT$+KDkWJ}<pWJ2O;~QgRgv^k+pDiwJ&nzrwPLw8OZmzjV+MFppO*Vye1y03K'
        'xuk88t7K`R)Y<bc_?<%UD6$!)z6XZD0wHM_a+hn(l=Rz`3(yEeCc5J-qzzsJZ?PhaU^Nj@s&Q3m9;Uq%R1gN%Kr!EvkgqU-J|?b`'
        'T578bX4!{cknYU#)fF-sMhUroZHhoAgpf-G_FSf*Dbg78b&)u2*raGNW^F%WWsRXwzzkOD_-b7$5}^AnSgZx}eXKCHTg&G&<?_nJ'
        '8t*15;4o12Xws<zG{yM@+X8c-a5jX(5J;l73fKq-vXSK|#BGvv_MMmzXN+`~HpR>0723f4B+ge`XZXDpx^nABD}|WK&i#a|=xNhs'
        'zd_wF8xO*0Gqj3q$Sxf!vePvw@U0jc4#{jAC5+rD`;+;#KVmT(g^*nwMLN80WSGweE)?jQc2b9D6Fod=JMD^ZF^WlXLd=Vq6bQxR'
        'U=+3!_lif^0eekuanHs=+0rXkvT<8Ssd70?_}q>e&_y<k;7g~-MsEYhZ{5bx$3Ra5uLE(22uXbing=#ik?n5Dq{zmW+c8w_8V{l('
        'I~k`AY+)OCKlRaamuumLp^9Qb6K1W*&ODQ5ty$}Wg=s4iB(@1#Fb(b@5!hy{7LTADzg?-eK3X7X0s97+AX2~!m~QM~*xn4bZn7Dv'
        '2Q%f~&^<QG>Xk;JXA-e(uYrQdPb)Sk$)IZoehAqTu-hQNQ2<ou8N=AQP6V2Or)oYfcjE@EiPVgaxhvOXPshVi@qk;%%8m~yI#+j0'
        'm&76H<mul<w(t8gdAIz1mv`DZ+igd2k&%8%bUSb&s1IcICe+K&<1N^iEQwV2FdDL50Yp%U53+-|nTIU7W07!hb|v+FI0&Ae6^kDi'
        'leC#@2afc((ooQm)PXny8R7v40^34i7!Nt<7F0?H@V!P(cNyG`xGSf7%<n<Oft(JR@nJJQVsO-qk0B1_bgx;z4{;=?`w{o#^nh7^'
        '5OHr#51ILK#KD}tVDwBNzL3+yh=+1|1o1#lk0S2N=`qByoE|stzi8~9Fm_HFJ*SMl(}*W?dIs@CPG3TNF{cFacuvnE9?R*=h(~k!'
        '9mFF!eFgDwPG3cw$mu!b*LlS8oK715rVtP2^flw>cM<pJblUhkW8$@p->)N%=JbN`e-?2#r*kHbd6SO?6Hi&!-8o${aa}a|ZJPKl'
        'RduIt7<|*<_Y7V(_?E%94PG&L!{9xG!r+#{hX$V*{KVj=20t_SrNOTZeqG_skpUwduZ784Xx74wTDVsWq87Gl;bAR2sfAB!;nQ09'
        'tQNkkg|BMiYa^s^&x5l8P81}0Gv*-0!`U;MbZ?$hSp$!-&V94z;yV3JF4@%`*4(C_y2JM9JZUb&T3RVwi7bYPv31vFeyyVC8r-Ad'
        'R5p4Yj{0QV-4;$(0w?R7IR6mB4Oj~_rg*KroSmOvxG>k8n_pO3nr|-7HJgi<nzOSPFD%S9=NFm_i?d6Y<`x$gs*|rw%8+87gfm1;'
        'i7!%ziK{?1e-(e!V)>D{wjzEYZcK`I#191(?~0pZMcm4EX$ka-VZgUQ8Ay>GtU}p-)QHtbs8zf#eq52*Ples#I<F&%9)=^paKcAo'
        '69EJn!v6^7ez(#o;vujI<fiQMo2mS=DLsE?+RyDwd-?7L_aj%rwea~B_|uM@i$DKQi5{;KZ3DC0=F_1k=j;0i8jbZKc=XS__?!59'
        'H~u<?Lj2>~Pj=T>|75?`C)vz(xsS&g?wbE&!cXl;c)#3FWA0yle(n!HE2M8T|9uRWu5)yKQv6H&Vf_@iF8;m#CWdhu9%-L2vfV&!'
        'uxU$j!^>$!Z*b@A5*%ETYl?$yU6CAY>e;8Zb$0BIS!F)H;M;(~XO2}oF9UYZb>|3tKj4KreCE9=8?CNQa8t!UP5gIl>$f2A^2hoe'
        'kov9vXP<<xABLB>#)&I1aiufSS-*XFeZI5)K1|%-xqkbwDd=GJA+xQ5pNsMJHLT$8`_*mzGFJ92e7ud1EBLqyk8HgDQ_nL>^!#T0'
        'rpdeC39bpjHM_~U(MiS=n0T@?8QX_38P<OQ<0-U&8WR8j'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

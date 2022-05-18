# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/jeroboam_datatypes/actuators/servo/ServoConfig.0.1.uavcan
#
# Generated at:  2022-05-18 08:39:38.951166 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     jeroboam_datatypes.actuators.servo.ServoConfig
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import jeroboam_datatypes.actuators.motion


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class ServoConfig_0_1:
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
                 ID:           None | int | _np_.uint8 = None,
                 torque_limit: None | int | _np_.uint16 = None,
                 moving_speed: None | int | _np_.uint16 = None,
                 pid:          None | jeroboam_datatypes.actuators.motion.PIDConfig_0_1 = None) -> None:
        """
        jeroboam_datatypes.actuators.servo.ServoConfig.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param ID:           saturated uint8 ID
        :param torque_limit: saturated uint16 torque_limit
        :param moving_speed: saturated uint16 moving_speed
        :param pid:          jeroboam_datatypes.actuators.motion.PIDConfig.0.1 pid
        """
        self._ID:           int
        self._torque_limit: int
        self._moving_speed: int
        self._pid:          jeroboam_datatypes.actuators.motion.PIDConfig_0_1

        self.ID = ID if ID is not None else 0  # type: ignore

        self.torque_limit = torque_limit if torque_limit is not None else 0  # type: ignore

        self.moving_speed = moving_speed if moving_speed is not None else 0  # type: ignore

        if pid is None:
            self.pid = jeroboam_datatypes.actuators.motion.PIDConfig_0_1()
        elif isinstance(pid, jeroboam_datatypes.actuators.motion.PIDConfig_0_1):
            self.pid = pid
        else:
            raise ValueError(f'pid: expected jeroboam_datatypes.actuators.motion.PIDConfig_0_1 '
                             f'got {type(pid).__name__}')

    @property
    def ID(self) -> int:
        """
        saturated uint8 ID
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._ID

    @ID.setter
    def ID(self, x: int | _np_.uint8) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 255:
            self._ID = x
        else:
            raise ValueError(f'ID: value {x} is not in [0, 255]')

    @property
    def torque_limit(self) -> int:
        """
        saturated uint16 torque_limit
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._torque_limit

    @torque_limit.setter
    def torque_limit(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._torque_limit = x
        else:
            raise ValueError(f'torque_limit: value {x} is not in [0, 65535]')

    @property
    def moving_speed(self) -> int:
        """
        saturated uint16 moving_speed
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._moving_speed

    @moving_speed.setter
    def moving_speed(self, x: int | _np_.uint16) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 65535:
            self._moving_speed = x
        else:
            raise ValueError(f'moving_speed: value {x} is not in [0, 65535]')

    @property
    def pid(self) -> jeroboam_datatypes.actuators.motion.PIDConfig_0_1:
        """
        jeroboam_datatypes.actuators.motion.PIDConfig.0.1 pid
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._pid

    @pid.setter
    def pid(self, x: jeroboam_datatypes.actuators.motion.PIDConfig_0_1) -> None:
        if isinstance(x, jeroboam_datatypes.actuators.motion.PIDConfig_0_1):
            self._pid = x
        else:
            raise ValueError(f'pid: expected jeroboam_datatypes.actuators.motion.PIDConfig_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u8(max(min(self.ID, 255), 0))
        _ser_.add_aligned_u16(max(min(self.torque_limit, 65535), 0))
        _ser_.add_aligned_u16(max(min(self.moving_speed, 65535), 0))
        _ser_.pad_to_alignment(8)
        self.pid._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 168 <= (_ser_.current_bit_length - _base_offset_) <= 168, \
            'Bad serialization of jeroboam_datatypes.actuators.servo.ServoConfig.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> ServoConfig_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "ID"
        _f0_ = _des_.fetch_aligned_u8()
        # Temporary _f1_ holds the value of "torque_limit"
        _f1_ = _des_.fetch_aligned_u16()
        # Temporary _f2_ holds the value of "moving_speed"
        _f2_ = _des_.fetch_aligned_u16()
        # Temporary _f3_ holds the value of "pid"
        _des_.pad_to_alignment(8)
        _f3_ = jeroboam_datatypes.actuators.motion.PIDConfig_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = ServoConfig_0_1(
            ID=_f0_,
            torque_limit=_f1_,
            moving_speed=_f2_,
            pid=_f3_)
        _des_.pad_to_alignment(8)
        assert 168 <= (_des_.consumed_bit_length - _base_offset_) <= 168, \
            'Bad deserialization of jeroboam_datatypes.actuators.servo.ServoConfig.0.1'
        assert isinstance(self, ServoConfig_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'ID=%s' % self.ID,
            'torque_limit=%s' % self.torque_limit,
            'moving_speed=%s' % self.moving_speed,
            'pid=%s' % self.pid,
        ])
        return f'jeroboam_datatypes.actuators.servo.ServoConfig.0.1({_o_0_})'

    _EXTENT_BYTES_ = 21

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8%CLlD0{^vD-ESL35O+RIoHnItU7`XK4OF5=qSrXFgZqM15=DxxO|69T1lsQ1Z9GfwtG9cWT?k5rsIatBDzZpC^VC0+S)ae+'
        'j|d*HWZ!!CH?uRp-^|?U;-6=QT=%2y#BEP_zC{E}IQ97}>iEneZWP3k;F4)|?MNo6E7OF1+m4w&*I&HWC%UBaB%}eJTR*ZSav~ZK'
        'k4h>LBP@z|Dx*YL=(ZVIN9K1Y3Xge1s{(1VMDQrokW)+F_15Rw&e?Ns^lPoI5-MfFom4WRf559|1UW!ymEYsc_lCh;=>|hgG<ueK'
        'obZ54-b6(4StxiTWZr%#S%W1PGrdY2E{V^=h6HUF(78*6Bthgc4Y$-<z3<4FSvz?4#2lH7e$$6q-6BHL(4&br>ge~>fxMdE-_>f7'
        'c#*4BPUF^Ub}1BLt+)EnUWJd~6S$LEtRSy1Q$~DqsfJJCvwvk3L`@zxh=>{UCavastGv2@shmM1Q7o&zzuQw2mSDLr9IT*NL#OKF'
        '8L}k_Z6hmtyv4l7T{0e-t&5~zBg|(33uPuE^1Qs~M^s)wVV3K?EK!w!HbO2_q+Tr_Cm1w_DzM)6dTTUO_qHk<o3+iY%J%kFt-4vO'
        'RUg*M<*zm><=R%IR;iY^A8uAFl?`o_OC7b0TF2DovaRg}6w2|@<LCXvhH_$#a{RwmE8lRLWq5>tdr_+e62)4r&vGK#ffM;03!?ah'
        '1rgF_f`1yb#Aq;N=sn^B$D)V2x_QWACi!&SJb8h!!!yKPKS+I_Chc($`f5@?W%^8)?De<8!ORy)z(Z|6Hw)S_izQR?sZWhpd(J>}'
        'Z|y?%Op$-qifPzw=7ZERKCqk?Vm_tZzMhZ|9>MN^6$jlfI-H80f2N8fgM&EjY(SZN0ICoJPqCFf7AMT561$+I-Y3VV2uU0zl3<_*'
        '>IM-}nz#%Pd`4o5jjEQ+!{-i`RUL<7t8RABk=eNi*t-y!DL5Z<t*-2}W1#*ns;1S=$wop4gH}S$vu46h7_^hMVU?|vHeDKOX+}qp'
        '02LTUVj98BQtmR{G5NwiJnpgxPvNjfXIJ7n^*rqKi8{d3QQQZ3qoE<3T3x2@O>yD9W&)2`b_S~>oaAwKnYQOp4r)IK2fyx#?w5st'
        '2G#<6pG8Xg<;8?SpCbBn3i>a*kX~{=Sy>ETnvmAv2Hb<Y@FkSsZ@8a==zu(c6j~){!z=g+eufkHMdiCMC9T#*UQ6T5!>^aH+?m4Y'
        'SqA%K7F+)Za+KBr(u&MwIuww(f?;lw{?!5fw-I!E2<qF8ZBMr?A*eKJn<+N7{U!sy!`*k2;EUTvRqG$;51`zd2mk;'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/jeroboam_datatypes/actuators/servo/SliderConfig.0.1.uavcan
#
# Generated at:  2022-05-18 08:39:39.011965 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     jeroboam_datatypes.actuators.servo.SliderConfig
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
class SliderConfig_0_1:
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
                 ID:                None | int | _np_.uint8 = None,
                 speed_pi:          None | jeroboam_datatypes.actuators.motion.PIDConfig_0_1 = None,
                 position_pid:      None | jeroboam_datatypes.actuators.motion.PIDConfig_0_1 = None,
                 feedforward_gains: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        jeroboam_datatypes.actuators.servo.SliderConfig.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param ID:                saturated uint8 ID
        :param speed_pi:          jeroboam_datatypes.actuators.motion.PIDConfig.0.1 speed_pi
        :param position_pid:      jeroboam_datatypes.actuators.motion.PIDConfig.0.1 position_pid
        :param feedforward_gains: saturated float32[2] feedforward_gains
        """
        self._ID:                int
        self._speed_pi:          jeroboam_datatypes.actuators.motion.PIDConfig_0_1
        self._position_pid:      jeroboam_datatypes.actuators.motion.PIDConfig_0_1
        self._feedforward_gains: _NDArray_[_np_.float32]

        self.ID = ID if ID is not None else 0  # type: ignore

        if speed_pi is None:
            self.speed_pi = jeroboam_datatypes.actuators.motion.PIDConfig_0_1()
        elif isinstance(speed_pi, jeroboam_datatypes.actuators.motion.PIDConfig_0_1):
            self.speed_pi = speed_pi
        else:
            raise ValueError(f'speed_pi: expected jeroboam_datatypes.actuators.motion.PIDConfig_0_1 '
                             f'got {type(speed_pi).__name__}')

        if position_pid is None:
            self.position_pid = jeroboam_datatypes.actuators.motion.PIDConfig_0_1()
        elif isinstance(position_pid, jeroboam_datatypes.actuators.motion.PIDConfig_0_1):
            self.position_pid = position_pid
        else:
            raise ValueError(f'position_pid: expected jeroboam_datatypes.actuators.motion.PIDConfig_0_1 '
                             f'got {type(position_pid).__name__}')

        if feedforward_gains is None:
            self.feedforward_gains = _np_.zeros(2, _np_.float32)
        else:
            if isinstance(feedforward_gains, _np_.ndarray) and feedforward_gains.dtype == _np_.float32 and feedforward_gains.ndim == 1 and feedforward_gains.size == 2:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._feedforward_gains = feedforward_gains
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                feedforward_gains = _np_.array(feedforward_gains, _np_.float32).flatten()
                if not feedforward_gains.size == 2:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'feedforward_gains: invalid array length: not {feedforward_gains.size} == 2')
                self._feedforward_gains = feedforward_gains
            assert isinstance(self._feedforward_gains, _np_.ndarray)
            assert self._feedforward_gains.dtype == _np_.float32  # type: ignore
            assert self._feedforward_gains.ndim == 1
            assert len(self._feedforward_gains) == 2

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
    def speed_pi(self) -> jeroboam_datatypes.actuators.motion.PIDConfig_0_1:
        """
        jeroboam_datatypes.actuators.motion.PIDConfig.0.1 speed_pi
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._speed_pi

    @speed_pi.setter
    def speed_pi(self, x: jeroboam_datatypes.actuators.motion.PIDConfig_0_1) -> None:
        if isinstance(x, jeroboam_datatypes.actuators.motion.PIDConfig_0_1):
            self._speed_pi = x
        else:
            raise ValueError(f'speed_pi: expected jeroboam_datatypes.actuators.motion.PIDConfig_0_1 got {type(x).__name__}')

    @property
    def position_pid(self) -> jeroboam_datatypes.actuators.motion.PIDConfig_0_1:
        """
        jeroboam_datatypes.actuators.motion.PIDConfig.0.1 position_pid
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._position_pid

    @position_pid.setter
    def position_pid(self, x: jeroboam_datatypes.actuators.motion.PIDConfig_0_1) -> None:
        if isinstance(x, jeroboam_datatypes.actuators.motion.PIDConfig_0_1):
            self._position_pid = x
        else:
            raise ValueError(f'position_pid: expected jeroboam_datatypes.actuators.motion.PIDConfig_0_1 got {type(x).__name__}')

    @property
    def feedforward_gains(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[2] feedforward_gains
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._feedforward_gains

    @feedforward_gains.setter
    def feedforward_gains(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 2:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._feedforward_gains = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 2:  # Length cannot be checked before casting and flattening
                raise ValueError(f'feedforward_gains: invalid array length: not {x.size} == 2')
            self._feedforward_gains = x
        assert isinstance(self._feedforward_gains, _np_.ndarray)
        assert self._feedforward_gains.dtype == _np_.float32  # type: ignore
        assert self._feedforward_gains.ndim == 1
        assert len(self._feedforward_gains) == 2

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_u8(max(min(self.ID, 255), 0))
        _ser_.pad_to_alignment(8)
        self.speed_pi._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.position_pid._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.feedforward_gains) == 2, 'self.feedforward_gains: saturated float32[2]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.feedforward_gains)
        _ser_.pad_to_alignment(8)
        assert 328 <= (_ser_.current_bit_length - _base_offset_) <= 328, \
            'Bad serialization of jeroboam_datatypes.actuators.servo.SliderConfig.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> SliderConfig_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "ID"
        _f0_ = _des_.fetch_aligned_u8()
        # Temporary _f1_ holds the value of "speed_pi"
        _des_.pad_to_alignment(8)
        _f1_ = jeroboam_datatypes.actuators.motion.PIDConfig_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "position_pid"
        _des_.pad_to_alignment(8)
        _f2_ = jeroboam_datatypes.actuators.motion.PIDConfig_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f3_ holds the value of "feedforward_gains"
        _f3_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 2)
        assert len(_f3_) == 2, 'saturated float32[2]'
        self = SliderConfig_0_1(
            ID=_f0_,
            speed_pi=_f1_,
            position_pid=_f2_,
            feedforward_gains=_f3_)
        _des_.pad_to_alignment(8)
        assert 328 <= (_des_.consumed_bit_length - _base_offset_) <= 328, \
            'Bad deserialization of jeroboam_datatypes.actuators.servo.SliderConfig.0.1'
        assert isinstance(self, SliderConfig_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'ID=%s' % self.ID,
            'speed_pi=%s' % self.speed_pi,
            'position_pid=%s' % self.position_pid,
            'feedforward_gains=%s' % _np_.array2string(self.feedforward_gains, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'jeroboam_datatypes.actuators.servo.SliderConfig.0.1({_o_0_})'

    _EXTENT_BYTES_ = 41

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8%dmuE0{^vD-ESL35Vw=KvD*|#T|j_D1E>&$xO_RO%L9}qSc#6LRzjgXl<l5x?b-Ie*xNHPqH6k3lt?S6ltlv3cV77unZ5H@'
        'VkZ(3Sh8=t^V`{(-~49pVCuIErCj<^*P@OayPid2COGx@kJRy)MH-<Wg)x^*tIK;*Bn_De_Ejfh`dEMXR6o}9sz3tjqkrKc6QL7Q'
        'pSV;~iI~`;h^I0Xv4vsVp|$66mx=W-X!4d;Mbc&>=3$^Ar>4K|+Q-_?+4-OKQ>`u$Dy85~B3Z2O<5_29*+*$rsBz}GgX}J**$|VC'
        'K5Kg<xX&eTBcgmah<Phu?p7dKi;0t^ULp>c#A88Ag0_noyg_40{Lp0@uBzASy+CH0wT`}R<1!UJ)4N(-C9$M|ONBce=rD1hpeD99'
        'w3;Gr*w8Acap{%pP$<Jh*D9!w&*j(;B@$@Ww>G*A!!(q7WWo#*I0&lVI)h3fXa_T`@qOlgnI`zTSvpC?Wx_n>vp{CVV(q1x7gBiw'
        '1#j4M@Fu(s*A9^>pSA)n6Qo0xngWx?RAbaYt!v{p^}$MIak;v@QdwJDsje<ptE)GwOG`HvD@)atO0}}Ow03iOwNhEshRwuLCFDP%'
        '4K6#{o<#B-4<o+cD{Me9)+kT^*J|cAmsy2-__v$2nj~SQ)!bP@;*Rfx9>*q?x0xRzZ6^6U5fi2d1BNb;25=N2)YO$-7BR`k<0i->'
        '%pGjRy}Xln9u=L_AdJ<fUc&URdfuLU9y?h16!CeW?FYu7`^K0yGE6*bqS|=_%{{k^*)u`@*?vTWbij5J$HYK6O-39ud<Wh=A-Bp%'
        '```wA@^71i;inu<<8FMW%0t6UoKALYm~*~^kDv)8!SQlgBv^w==ISH$5@{L{k|-3CV4^!}mc(Hq8VnsCBN4^nQPbw(aR+5p$D3-u'
        'ZdQ+x+57^|6NKh!nuxeo7uP!xP;Udfrqz|vLBat2Q9{nMVZur1kCU}%Em;X|H)x=x8Rs$q8e<y541&4fc!TL9Q!ji5w^J733)t+^'
        'nYOr2U6%)~5gnj+822ikXlMw=s>|r!hzrj(x8l&wCw*%RZ`UY0Oxt;E$2ax^xQE|wAM2hhVz`f5fZZ(9yFGca*q{#(eJ}?7i(O34'
        '@pqL~j3Z`R$4BLL9o;kOO9e|KV->j2wU+-YEq-cGjBm+y*Qz7H9$_La^cEI+D=joXrqJ0Y*4Yfj59U&DQ6BUK4=odT4rbwZcn|)B'
        'Kj3e8kpMq}hdb~Hf_Vrbg6}~<3{n-+7o=9N55FQ$D-Js6sO!lXB|Xbvhi9qe|3D6tSVR*0iYX$IMMGpJq@OaK9pdWYV6_K6wVZ*s'
        'i+Q+beum(wwnrU*Wg9ll`euG4{)of0)A|Qv3jX8~2><{'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

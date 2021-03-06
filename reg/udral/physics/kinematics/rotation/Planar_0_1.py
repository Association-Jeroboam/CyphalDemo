# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/physics/kinematics/rotation/Planar.0.1.dsdl
#
# Generated at:  2022-05-06 20:34:35.044170 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.kinematics.rotation.Planar
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.si.unit.angle
import uavcan.si.unit.angular_acceleration
import uavcan.si.unit.angular_velocity


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Planar_0_1:
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
                 angular_position:     None | uavcan.si.unit.angle.Scalar_1_0 = None,
                 angular_velocity:     None | uavcan.si.unit.angular_velocity.Scalar_1_0 = None,
                 angular_acceleration: None | uavcan.si.unit.angular_acceleration.Scalar_1_0 = None) -> None:
        """
        reg.udral.physics.kinematics.rotation.Planar.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param angular_position:     uavcan.si.unit.angle.Scalar.1.0 angular_position
        :param angular_velocity:     uavcan.si.unit.angular_velocity.Scalar.1.0 angular_velocity
        :param angular_acceleration: uavcan.si.unit.angular_acceleration.Scalar.1.0 angular_acceleration
        """
        self._angular_position:     uavcan.si.unit.angle.Scalar_1_0
        self._angular_velocity:     uavcan.si.unit.angular_velocity.Scalar_1_0
        self._angular_acceleration: uavcan.si.unit.angular_acceleration.Scalar_1_0

        if angular_position is None:
            self.angular_position = uavcan.si.unit.angle.Scalar_1_0()
        elif isinstance(angular_position, uavcan.si.unit.angle.Scalar_1_0):
            self.angular_position = angular_position
        else:
            raise ValueError(f'angular_position: expected uavcan.si.unit.angle.Scalar_1_0 '
                             f'got {type(angular_position).__name__}')

        if angular_velocity is None:
            self.angular_velocity = uavcan.si.unit.angular_velocity.Scalar_1_0()
        elif isinstance(angular_velocity, uavcan.si.unit.angular_velocity.Scalar_1_0):
            self.angular_velocity = angular_velocity
        else:
            raise ValueError(f'angular_velocity: expected uavcan.si.unit.angular_velocity.Scalar_1_0 '
                             f'got {type(angular_velocity).__name__}')

        if angular_acceleration is None:
            self.angular_acceleration = uavcan.si.unit.angular_acceleration.Scalar_1_0()
        elif isinstance(angular_acceleration, uavcan.si.unit.angular_acceleration.Scalar_1_0):
            self.angular_acceleration = angular_acceleration
        else:
            raise ValueError(f'angular_acceleration: expected uavcan.si.unit.angular_acceleration.Scalar_1_0 '
                             f'got {type(angular_acceleration).__name__}')

    @property
    def angular_position(self) -> uavcan.si.unit.angle.Scalar_1_0:
        """
        uavcan.si.unit.angle.Scalar.1.0 angular_position
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._angular_position

    @angular_position.setter
    def angular_position(self, x: uavcan.si.unit.angle.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.angle.Scalar_1_0):
            self._angular_position = x
        else:
            raise ValueError(f'angular_position: expected uavcan.si.unit.angle.Scalar_1_0 got {type(x).__name__}')

    @property
    def angular_velocity(self) -> uavcan.si.unit.angular_velocity.Scalar_1_0:
        """
        uavcan.si.unit.angular_velocity.Scalar.1.0 angular_velocity
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._angular_velocity

    @angular_velocity.setter
    def angular_velocity(self, x: uavcan.si.unit.angular_velocity.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.angular_velocity.Scalar_1_0):
            self._angular_velocity = x
        else:
            raise ValueError(f'angular_velocity: expected uavcan.si.unit.angular_velocity.Scalar_1_0 got {type(x).__name__}')

    @property
    def angular_acceleration(self) -> uavcan.si.unit.angular_acceleration.Scalar_1_0:
        """
        uavcan.si.unit.angular_acceleration.Scalar.1.0 angular_acceleration
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._angular_acceleration

    @angular_acceleration.setter
    def angular_acceleration(self, x: uavcan.si.unit.angular_acceleration.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.angular_acceleration.Scalar_1_0):
            self._angular_acceleration = x
        else:
            raise ValueError(f'angular_acceleration: expected uavcan.si.unit.angular_acceleration.Scalar_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.angular_position._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.angular_velocity._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.angular_acceleration._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of reg.udral.physics.kinematics.rotation.Planar.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Planar_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "angular_position"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.unit.angle.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "angular_velocity"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.angular_velocity.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f2_ holds the value of "angular_acceleration"
        _des_.pad_to_alignment(8)
        _f2_ = uavcan.si.unit.angular_acceleration.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Planar_0_1(
            angular_position=_f0_,
            angular_velocity=_f1_,
            angular_acceleration=_f2_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of reg.udral.physics.kinematics.rotation.Planar.0.1'
        assert isinstance(self, Planar_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'angular_position=%s' % self.angular_position,
            'angular_velocity=%s' % self.angular_velocity,
            'angular_acceleration=%s' % self.angular_acceleration,
        ])
        return f'reg.udral.physics.kinematics.rotation.Planar.0.1({_o_0_})'

    _EXTENT_BYTES_ = 12

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8TZVOF0{^{LTW?!M5O&(!TWF&ckZ1*lht$yO)OPIPa18_n2@_))iiFg%*>iU5S#fUK-DBCHN>p6bNGpMq<%LIn1QI`j|HSM$'
        'cAO?Lk&qygl{quBv)_Dk+3#k5{cEw5|CyK5AyX{$h~iSvP<%uEkb5LZqBK!Lb8DX2(=rQmCi&;Xl-oo5+GG33R?HlUX@vIMlJ~rf'
        'Ng8@743!9!_qB+5M70xTqESd<uN%^sN^2HLpG$=r3njDg#YjH1?NWQ@C;Ql%ON44Ig`a7z>;t@L3dAEXYvy(Y57`9TGGSCxq8(ni'
        'P$*%}T+e7fps}Zfm&HPRH11)by?}-Y3>ILiJ<~2Z3~>2@g{z};tJ46aQba<FJ_1<U2@|TH=I0Xeg(e}7dm3!JjGzLlG>H<1pl+Dw'
        'yW`{Tn756#U1xGk{All5bB!oXV@4%A9_R_iiD(buXUtvvP}0EhtB~29k&H3S&GkmL-m0%RHa6B<&3dcV+-%iqZ&Vw#)_SAWXx271'
        '>&-@^YTaF#kL=7#$^?zAnI$X<tSO<In$=^~ApWqZ`6CN=;6;TgGM-8vP|cY=Fwc^QV!#<m6RC+{wqsU^N-`O6G=!X_6caED?q4W;'
        '1mDFL8+4ua5DA;PgLgyXdg?+dtXbY3ra;3Fd6ZalJ<a@31O%Hc3*CK_5@YJ~MP>1z!h^G}y4V$YeXY4tRM@L|RnOJYYDe!X0jdy^'
        '<gs>z?Tdih1E@j`3GhP<x;8HRgno3?C%>(^{DIJ)<llSvIcflNktC@#<!M3GF!B@32$Ae!hS*fDbf2bNQk}?28_kmd1U5Hx%#|)>'
        'OvJrYPO#^!oh-yOhbOHVp-;n%+n;TvUH(P+ID%;r$hH?VAJdIQ>^c+$I&i{*>r$lIon9t<kkUAx(oW_pKW~<+$SpcZl5dH8nvpp)'
        '9Zk)#xm!Cuclp^q50gOX;rSy7FO8&E+GThZ*5Kw7sKBj%(d8>emlGrj>kuR{8zHAq$F|lGDQFx(vjZEjS%Ej<EqEK=fp_6O*n;;b'
        'd5^JM*mms%J9+ECNAPiu6n3F|RGWK8(wBwt{<swIm8$>{%xWKh6m7v7Bu_4zPV(zhNTxx+L)Q^*3IC5o-#A6|G|msf{3GYr&PwIK'
        '<bBG8Ib`l2SAf9^d=DIchaa*tv73vysc;A752IUp#nXuMG<h6xWsjdn+)~8@i94z`*;09W=7qZ>uQK(MOqVGN1ED;7UfSJb>*2ZW'
        'BzB8BK6B5QrDDzCHgs?9Inn+oF8y<w=Vw#+g>SiX+AY*>O|)a@6YAdz=Y7=fpLTv)?JDQ}4Gzu6lh_CV00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

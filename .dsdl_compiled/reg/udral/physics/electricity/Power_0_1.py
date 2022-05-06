# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/physics/electricity/Power.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.356998 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.electricity.Power
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.si.unit.electric_current
import uavcan.si.unit.voltage


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Power_0_1:
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
                 current: None | uavcan.si.unit.electric_current.Scalar_1_0 = None,
                 voltage: None | uavcan.si.unit.voltage.Scalar_1_0 = None) -> None:
        """
        reg.udral.physics.electricity.Power.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param current: uavcan.si.unit.electric_current.Scalar.1.0 current
        :param voltage: uavcan.si.unit.voltage.Scalar.1.0 voltage
        """
        self._current: uavcan.si.unit.electric_current.Scalar_1_0
        self._voltage: uavcan.si.unit.voltage.Scalar_1_0

        if current is None:
            self.current = uavcan.si.unit.electric_current.Scalar_1_0()
        elif isinstance(current, uavcan.si.unit.electric_current.Scalar_1_0):
            self.current = current
        else:
            raise ValueError(f'current: expected uavcan.si.unit.electric_current.Scalar_1_0 '
                             f'got {type(current).__name__}')

        if voltage is None:
            self.voltage = uavcan.si.unit.voltage.Scalar_1_0()
        elif isinstance(voltage, uavcan.si.unit.voltage.Scalar_1_0):
            self.voltage = voltage
        else:
            raise ValueError(f'voltage: expected uavcan.si.unit.voltage.Scalar_1_0 '
                             f'got {type(voltage).__name__}')

    @property
    def current(self) -> uavcan.si.unit.electric_current.Scalar_1_0:
        """
        uavcan.si.unit.electric_current.Scalar.1.0 current
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._current

    @current.setter
    def current(self, x: uavcan.si.unit.electric_current.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.electric_current.Scalar_1_0):
            self._current = x
        else:
            raise ValueError(f'current: expected uavcan.si.unit.electric_current.Scalar_1_0 got {type(x).__name__}')

    @property
    def voltage(self) -> uavcan.si.unit.voltage.Scalar_1_0:
        """
        uavcan.si.unit.voltage.Scalar.1.0 voltage
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._voltage

    @voltage.setter
    def voltage(self, x: uavcan.si.unit.voltage.Scalar_1_0) -> None:
        if isinstance(x, uavcan.si.unit.voltage.Scalar_1_0):
            self._voltage = x
        else:
            raise ValueError(f'voltage: expected uavcan.si.unit.voltage.Scalar_1_0 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.current._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.voltage._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 64 <= (_ser_.current_bit_length - _base_offset_) <= 64, \
            'Bad serialization of reg.udral.physics.electricity.Power.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Power_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "current"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.si.unit.electric_current.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "voltage"
        _des_.pad_to_alignment(8)
        _f1_ = uavcan.si.unit.voltage.Scalar_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = Power_0_1(
            current=_f0_,
            voltage=_f1_)
        _des_.pad_to_alignment(8)
        assert 64 <= (_des_.consumed_bit_length - _base_offset_) <= 64, \
            'Bad deserialization of reg.udral.physics.electricity.Power.0.1'
        assert isinstance(self, Power_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'current=%s' % self.current,
            'voltage=%s' % self.voltage,
        ])
        return f'reg.udral.physics.electricity.Power.0.1({_o_0_})'

    _EXTENT_BYTES_ = 8

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{@*=>rdQ95I@4>fTVedwjcW3wh}qi)ZyTuNBSZGkyO_Z5~8T8gtlvY?`G9K+x4ywTotMLkSa(kH4@wZx3l)WAVHCO'
        '(#h+YotfXv{AT>u)W4P4O7SzFCV8kr=~2Z~!KC<u`I37yh`ULwgyz<~v#--E&{@i#<_Wi_cIml2wly<NBi2Rz7b)*}S(q~EC6Fr-'
        'D341X=u`wk=iXj?$Wv=(X^*E$#F2%HsXptUPi?Exn)us3x8^cs8g2Ycb7c?E{{_f~x2&1o5nP5NMDsLcno;dw!lhCO(`GSay?{lY'
        '5?&SwJw!)?EKPZ&z5RemmRhL7Tx+6Lad6<ufraaR7Yi3*Nm9`jTJ#Xh+>VTyK3k#7)EAmc9(6R>7D0RgQ<`?;5b=Fv-rpOTJ2P(!'
        'bq}4&73GC}V$Hi$X%>Yn4aXh5L_b~D!A!Ey1#YJ-&{#}`Mc(P3(TBOY+E`v`uB<lJ*H@csE6wKGMzdc3dbv?=t~Q#Dwfg$T%37nb'
        'Y+bC($3o4pZo*UaIYq-bu%?1yW){X8L;bw$`mu%E@PWb<L!P8OV48>a#9XCqal}KK#Hpqtw7cd8RdJRE92Jt&gkb`v>K;<~2!0Pq'
        'cC_cDr&zFw+ZY>S$Eq2PPlh>7c7(QOek)Ia$!*?^t@$v?e2M)-;$_lB9`zj!X3BP3b4dww=UQ&f_47@)=33cyukI~-uDMpbnlDgb'
        '3URtSuG>8kaC-vFP{*qH68$d@xG?GoUexE`t+{ef=%0%BeSGb+!c5XQv4&jaMCDyS#^eymLrfN#=KA>v`@(dbj<_{L0}x1lcx0~a'
        'u`m=-=e0}l)M<A!iD~BNwdkS8WXA13w$>uAl#e5tl#Xm`HuEvvu816M@xYGUq3WoM6?fM2lpiH5DyDch^OavPs5+>wD;P?K6ErrC'
        'AD<h?UMw~1@V8GPe9}LC)*|pZEW*u~P=hc32hpco%sxg2D@f)HA_a{TSlfkl*r>rB_y)d(@8Em*0XE?-+%wfaP7B+PC~&_Z1w4RO'
        'feLov@v!R8hNoXj<-wrHKwWL&SImIn-#^A$J6+|Kf^e*k!(atQ?l9JX!wq-=?d$@eW)cSiw_>r2-ISHv7+34qKDOp+v5}GV^%3oh'
        'Y<^y!s8qJMNSu<pTSSV8lYt>goDKOsW0A&<#g#|y^9TtgWqylj;G`W(86P5fNS^{kiB3d<IO^dGvV^cCk!X2mex8u8h#P#j`i9rr'
        'Xs$>*jk|@vbCFes);Wo|K8(}fh>nX(xN<{M<6g(RMHoiFuau+sl2^v~v3=Inz*?x0wa|*ob{U0-Wqd};oi%Xn;{xPqzEoy90E}KD'
        '-eE2Y&%TWZkH;qRy{$NM3p0A-Xq&lmvN4AH48GCZlh<ifum}F+%1Jj-x;c^#E}s=Us(Jqb`uxJv3kU!J'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
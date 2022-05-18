# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/reg/udral/service/actuator/common/sp/Vector6.0.1.dsdl
#
# Generated at:  2022-05-06 20:34:37.676904 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.service.actuator.common.sp.Vector6
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Vector6_0_1:
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
                 value: None | _NDArray_[_np_.float16] | list[float] = None) -> None:
        """
        reg.udral.service.actuator.common.sp.Vector6.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param value: saturated float16[6] value
        """
        self._value: _NDArray_[_np_.float16]

        if value is None:
            self.value = _np_.zeros(6, _np_.float16)
        else:
            if isinstance(value, _np_.ndarray) and value.dtype == _np_.float16 and value.ndim == 1 and value.size == 6:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._value = value
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                value = _np_.array(value, _np_.float16).flatten()
                if not value.size == 6:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'value: invalid array length: not {value.size} == 6')
                self._value = value
            assert isinstance(self._value, _np_.ndarray)
            assert self._value.dtype == _np_.float16  # type: ignore
            assert self._value.ndim == 1
            assert len(self._value) == 6

    @property
    def value(self) -> _NDArray_[_np_.float16]:
        """
        saturated float16[6] value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: _NDArray_[_np_.float16] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float16 and x.ndim == 1 and x.size == 6:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._value = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float16).flatten()
            if not x.size == 6:  # Length cannot be checked before casting and flattening
                raise ValueError(f'value: invalid array length: not {x.size} == 6')
            self._value = x
        assert isinstance(self._value, _np_.ndarray)
        assert self._value.dtype == _np_.float16  # type: ignore
        assert self._value.ndim == 1
        assert len(self._value) == 6

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.value) == 6, 'self.value: saturated float16[6]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.value)
        _ser_.pad_to_alignment(8)
        assert 96 <= (_ser_.current_bit_length - _base_offset_) <= 96, \
            'Bad serialization of reg.udral.service.actuator.common.sp.Vector6.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector6_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "value"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float16, 6)
        assert len(_f0_) == 6, 'saturated float16[6]'
        self = Vector6_0_1(
            value=_f0_)
        _des_.pad_to_alignment(8)
        assert 96 <= (_des_.consumed_bit_length - _base_offset_) <= 96, \
            'Bad deserialization of reg.udral.service.actuator.common.sp.Vector6.0.1'
        assert isinstance(self, Vector6_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'value=%s' % _np_.array2string(self.value, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'reg.udral.service.actuator.common.sp.Vector6.0.1({_o_0_})'

    _EXTENT_BYTES_ = 512

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8U50gH0{?wf-)|f>5Wb}O)uf?U0_g(}y$2|vs+J;XBoGKes*|eCg=^A=N^Nkw>&cC&_lIn6bca-_eE>C*B`U@Izl?V;O|IlP'
        '>9k&Z{LRca-?y*k{@Ge+)jxNu90?;-#0+T3mHdMz3L=&kSy>oq!MoK5pkzi%@px2%KlNX{_AmX0TVOKJL3?bu)jg}L)K(fML*`k|'
        'GlICQVGvb9a}`mVW0^w4DV*CvN0ccm^2n6YKBTm<>D>}L25n@K2kgcD@%q%qt$5}y|Ju71#;w&dsVo?O;HNe5F37w2t^_5{D_drQ'
        'Th44K*L^bOy4HN;-A7$H1hEbIz~WC~YqG~x1`0CB?HFuIEu{_|%43SS+EoR&lPD`Jk(Q}CiI3Y<U&@VTSs}pVEw|o3yB@AZTXfb7'
        'M}d<+{Vo;BjODrDT3iHrLpT{9<kD6mBtFtaJ8@}<<L-D(7;b*^{{4I3_<&R;?keRjc`EJ5#|v(bC5qy2pS5)kPaWF#-@Uu`v$PFa'
        'd-OVP&|P6g>0M_Uh#6%`p=9daS`V^<NDHO?Qi2W|xv04mCCw4Pb06+P307VnH_Kj7?f4_bUEisc;(GLc5Mdp2Re}H8Z^Z4lCZW#f'
        'SSE8HABF`VhQ(qSL8Uldh-X4%>#ZSDVOa9KR^?8WgsZsh<{LP=D++3)MO1RPc0s8u88v=*>G2V+8ydQRQbWqgTmHm-z>b2_SXpSx'
        'r0_fL1~WyaQ=kI{tmHIOw-_EuCN$1IIds?$yQkFi%$JlKi{Q7}QhK+%H7b#-2gGNPc$E;pjEqR#P`-2h({QiQHmRU?C}kLXltgmo'
        'Qevy|DPbELWP9w@=w9?y6h`W8P~jRwZm3Qj>~My1g1fkfU*l#?JARAbH$!Ts)8|6SeDI$U(&-QMAt;+;A1@KdaeRo|^zRW&{~htT'
        'g4eK(Hx4|mb9_7|7xz!_*ByL{&o=Nm9^h}t@DMpBn4&<yBOHX1@%OqsnllV7RqcDNwp*vUG@m@p5V)X6?QJsR+7lZ4AP4a<w=e)b'
        ';bQzW?%-$mc{~%Ggm>Ohc~koSc&o_6-1AF?9xNDiPCU}*Z3DXv#KR!K4oP(a>gF!b2k?JxSYR(|J@;C(bmJn}QmuO;wuRf&d0;kP'
        '8q2(<7)&_r&}rwA({MTZ7xLp<I!*=v00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
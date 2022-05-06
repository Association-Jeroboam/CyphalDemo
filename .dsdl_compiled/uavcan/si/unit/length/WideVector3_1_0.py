# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/unit/length/WideVector3.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.533757 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.unit.length.WideVector3
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class WideVector3_1_0:
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
                 meter: None | _NDArray_[_np_.float64] | list[float] = None) -> None:
        """
        uavcan.si.unit.length.WideVector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param meter: saturated float64[3] meter
        """
        self._meter: _NDArray_[_np_.float64]

        if meter is None:
            self.meter = _np_.zeros(3, _np_.float64)
        else:
            if isinstance(meter, _np_.ndarray) and meter.dtype == _np_.float64 and meter.ndim == 1 and meter.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter = meter
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter = _np_.array(meter, _np_.float64).flatten()
                if not meter.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter: invalid array length: not {meter.size} == 3')
                self._meter = meter
            assert isinstance(self._meter, _np_.ndarray)
            assert self._meter.dtype == _np_.float64  # type: ignore
            assert self._meter.ndim == 1
            assert len(self._meter) == 3

    @property
    def meter(self) -> _NDArray_[_np_.float64]:
        """
        saturated float64[3] meter
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter

    @meter.setter
    def meter(self, x: _NDArray_[_np_.float64] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float64 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float64).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter: invalid array length: not {x.size} == 3')
            self._meter = x
        assert isinstance(self._meter, _np_.ndarray)
        assert self._meter.dtype == _np_.float64  # type: ignore
        assert self._meter.ndim == 1
        assert len(self._meter) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        assert len(self.meter) == 3, 'self.meter: saturated float64[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter)
        _ser_.pad_to_alignment(8)
        assert 192 <= (_ser_.current_bit_length - _base_offset_) <= 192, \
            'Bad serialization of uavcan.si.unit.length.WideVector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> WideVector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "meter"
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float64, 3)
        assert len(_f0_) == 3, 'saturated float64[3]'
        self = WideVector3_1_0(
            meter=_f0_)
        _des_.pad_to_alignment(8)
        assert 192 <= (_des_.consumed_bit_length - _base_offset_) <= 192, \
            'Bad deserialization of uavcan.si.unit.length.WideVector3.1.0'
        assert isinstance(self, WideVector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'meter=%s' % _np_.array2string(self.meter, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.unit.length.WideVector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 24

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YXOOM<{5T4Dx@*qTEBMxu?E+||~zq_4NAZS6F?6OKw;DTChyEAU#8C!OHwG$~4Ie>`N5|Os~KM}u->YWL@39Kcn'
        'UsYdKef9Wt>#x7JCud*yq+3=))nt0Gy)%t_W{SpUx@_lNJ2-D+xcS)kW9i4<{;=$9JdIzxh|lBQu&ozn4)33h=D0MAY;f7Qa6W77'
        'V&?1YM_1V=w)AaJW4Nl1Z9lkn5$j3VeX`!4#_7g%@_T#{!wqe`?_Du^JH(&kWp4c|6vOtuvrTpG&UIZGZ?sQ7hL0~%?|ZY1;m*E0'
        'vDL#fKfg*>ZwGc$+s4lA!mq(D@ulnC+<A8l64&;d*7&zkZs@{!y&@w{?}LA(8N8mim5udB;lrah>Pano0B;BB2{@Vj79W9=dhljZ'
        'nZCLR^atR~%?x-Rt7Q0TZ%Pkb4#4sLdJh;s@r}s@%Up__V#<^t6my9bW}HYysH9jTM!Ar=LK4Bs30I8ex!}3Vv1C#xlyrzdQXxbX'
        'r%DRMRnEB*lt>|zR9Irp5KFg|V@4HW0^k`Xm=d8>4o9p&STQgGKcbvUjzz8n0&5s?DLBVO5hMj+oaG4Rh^m|tP-aMiF~yN$AVg^n'
        '*vT3tRDcvABxec>u8`t9r(l&(h!#SG&=nB`G0d2R;K5l6-b$=cj&qXdN@2ng_>PFciebVO;0hHJ`C}2TLAp9qI=_t5&9J451}Ogg'
        'O(mRX1d77Hdye6~ubp4j*JC)YYa(pwwu|A@%Rq+Zyl5L&#;|u_=PlG(%I5c-?G1F%d1dYBvUX7VH4h&=vYqwr|K+aeU%>bJ9?0D~'
        '9Gk}U%XftU>)14-jeo|w)BCT60wUkibGL}o*J)!;(q=bR?bsMlm~JG=$*TeC(4KT=an{I(W06$r?XW$!-u4l6s}=&80F@@}U1)Ay'
        'ELU^md8{ASw+HBx%67dijki^N8Q#}VQ*-LB?Y(wYJPfz>(2jj+;i0j*GtdQLH!Y1TpaYIzOr0F1+f#^n<4dqzw`nfzcvuZ&ZFA-z'
        'CD$J;yV^A00JCX6j0G^Qdpm=;!1DR<0EL~^M2q3d-~cX7HMm@NV7PN(vSm0!S;}Vgsb}|eZ3b|$Ps0PI#jz`Gd|4mVhjmutGsbIH'
        '%T<0>i8(S=<rcI5WDi~yjLmNK9H&=--u>z8`dj$F1DNTW^XwnuH~)Uk1poj'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/jeroboam/actuators/motion/AdaptativePIDConfig.0.1.uavcan
#
# Generated at:  2022-05-06 20:25:55.633019 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     jeroboam.actuators.motion.AdaptativePIDConfig
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import jeroboam.actuators.motion


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class AdaptativePIDConfig_0_1:
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
                 configs:    None | _NDArray_[_np_.object_] | list[jeroboam.actuators.motion.PIDConfig_0_1] = None,
                 thresholds: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        jeroboam.actuators.motion.AdaptativePIDConfig.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param configs:    jeroboam.actuators.motion.PIDConfig.0.1[3] configs
        :param thresholds: saturated float32[3] thresholds
        """
        self._configs:    _NDArray_[_np_.object_]
        self._thresholds: _NDArray_[_np_.float32]

        if configs is None:
            self.configs = _np_.array([jeroboam.actuators.motion.PIDConfig_0_1() for _ in range(3)], _np_.object_)
        else:
            if isinstance(configs, _np_.ndarray) and configs.dtype == _np_.object_ and configs.ndim == 1 and configs.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._configs = configs
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                configs = _np_.array(configs, _np_.object_).flatten()
                if not configs.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'configs: invalid array length: not {configs.size} == 3')
                self._configs = configs
            assert isinstance(self._configs, _np_.ndarray)
            assert self._configs.dtype == _np_.object_  # type: ignore
            assert self._configs.ndim == 1
            assert len(self._configs) == 3

        if thresholds is None:
            self.thresholds = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(thresholds, _np_.ndarray) and thresholds.dtype == _np_.float32 and thresholds.ndim == 1 and thresholds.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._thresholds = thresholds
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                thresholds = _np_.array(thresholds, _np_.float32).flatten()
                if not thresholds.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'thresholds: invalid array length: not {thresholds.size} == 3')
                self._thresholds = thresholds
            assert isinstance(self._thresholds, _np_.ndarray)
            assert self._thresholds.dtype == _np_.float32  # type: ignore
            assert self._thresholds.ndim == 1
            assert len(self._thresholds) == 3

    @property
    def configs(self) -> _NDArray_[_np_.object_]:
        """
        jeroboam.actuators.motion.PIDConfig.0.1[3] configs
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._configs

    @configs.setter
    def configs(self, x: _NDArray_[_np_.object_] | list[jeroboam.actuators.motion.PIDConfig_0_1]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.object_ and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._configs = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.object_).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'configs: invalid array length: not {x.size} == 3')
            self._configs = x
        assert isinstance(self._configs, _np_.ndarray)
        assert self._configs.dtype == _np_.object_  # type: ignore
        assert self._configs.ndim == 1
        assert len(self._configs) == 3

    @property
    def thresholds(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] thresholds
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._thresholds

    @thresholds.setter
    def thresholds(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._thresholds = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'thresholds: invalid array length: not {x.size} == 3')
            self._thresholds = x
        assert isinstance(self._thresholds, _np_.ndarray)
        assert self._thresholds.dtype == _np_.float32  # type: ignore
        assert self._thresholds.ndim == 1
        assert len(self._thresholds) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        assert len(self.configs) == 3, 'self.configs: jeroboam.actuators.motion.PIDConfig.0.1[3]'
        # Element offset: concat(pad(8,pad(8,{0})),repeat(<=2,pad(8,concat(pad(1,repeat(3,{32})),{32}))))
        for _elem0_ in self.configs:
            _ser_.pad_to_alignment(8)
            _elem0_._serialize_(_ser_)
            assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert len(self.thresholds) == 3, 'self.thresholds: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.thresholds)
        _ser_.pad_to_alignment(8)
        assert 480 <= (_ser_.current_bit_length - _base_offset_) <= 480, \
            'Bad serialization of jeroboam.actuators.motion.AdaptativePIDConfig.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> AdaptativePIDConfig_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "configs"
        _des_.pad_to_alignment(8)
        _f0_ = _np_.empty(3, _np_.object_)  # type: ignore
        for _i0_ in range(3):
            _des_.pad_to_alignment(8)
            _e0_ = jeroboam.actuators.motion.PIDConfig_0_1._deserialize_(_des_)
            assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
            _f0_[_i0_] = _e0_
        assert len(_f0_) == 3, 'jeroboam.actuators.motion.PIDConfig.0.1[3]'
        _des_.pad_to_alignment(8)
        # Temporary _f1_ holds the value of "thresholds"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = AdaptativePIDConfig_0_1(
            configs=_f0_,
            thresholds=_f1_)
        _des_.pad_to_alignment(8)
        assert 480 <= (_des_.consumed_bit_length - _base_offset_) <= 480, \
            'Bad deserialization of jeroboam.actuators.motion.AdaptativePIDConfig.0.1'
        assert isinstance(self, AdaptativePIDConfig_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'configs=%s' % _np_.array2string(self.configs, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
            'thresholds=%s' % _np_.array2string(self.thresholds, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'jeroboam.actuators.motion.AdaptativePIDConfig.0.1({_o_0_})'

    _EXTENT_BYTES_ = 60

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{^X5ZEG7x5SC&)vYn)D;xtfNT0u+d6mpR)*-<F8I5vWCwW>HJeSxsqyIX5Exx2mY?Fp$NU_)Etve1CH{nUQ%*Z!mY'
        'l+NlTSy80WLIu+8?aa>1^UO1=!^Pj;TP_Sf`h%n&q(SJAlu1rQ{sZ+w<`7>*iAcF(Mqjw6Wag_(vak9HGbiTSk$Gy?^%99`g!b!?'
        'm=vC%kwejoDj`!R5{ir1*$!x;sN!ALzO%a{;sf3>dYN>YOwnwhpiB3M>l5P^+~UvX$mnx~DkZs>DVCZCm}yRpV=tqZnw*8fX>F?{'
        'po$V@3)b(>IW8sb8-2OSdo1{Z#T^CPcI#!77YGYk#A1~PgERR)Ea?yD<32?TC0H2&gYyUm-Wmp2gDb<;JM#c0l1JRKXY@)l6jZ%j'
        '+BxEJMZ!Vl#w{agpQegLBEUL7(pTD}<Mx=dgSI_uvP}PE_7OQr6^#QbgULY8Fiu1}F;`h&6CX%~hoDmITywa_82aN{y|U5RsMWW&'
        'YK_f}Mq~3<qguULsaG4ddZWHs-MY20S+7@&&6Rn21*=P_&sE>J3wn`wAx6A90)AQma-gQ)jXr;ytGq||@O4OmULYbdx;!sP+K)UD'
        'a^L8+Jr)V1)fWF{!ldoiDUoN14;<wKpX*EeEMbbz_B%r!W9_hues8w2Fr>0S?S!$qG|ZU!)vUYa=c$Lt7fHlp<36+t+Ovz2ZBiCe'
        '8`UjZ*TQpmIe%uzKkFql9*jjR^K1;1+d{$vgCPQecnZkqgp#ffSJ&J!d;$*Kcm@@y{nr*@l0}cx)WA3JZRRn(HZh3A>*w=s^L!0u'
        'pzvLW5)4=(nNJl9%&~rh9N1wZiI9q5xh;K>q#~0(Lqo_&LQ!D4WFH~-P+V=iV|s17dxHEHZy-Pr_EI^k@QJ19g$~E|ukQ2{py4id'
        '5oI_UJPa@%Jv@>RAL@EMeon=yIvMTyG&aggevJT4u?%Sk8i%dReP)g=UTDCl0~X;k*dEe3Xmpzf0gpScr~$2$es5z&OG7+UV^;lE'
        'Vwl(7XcH%&j90huW=!&A#w}ty+U`TRi{JgHW+aXj?xP~W%`0t<M8;C<eTd$NGrWIsm$TQ{2l~2+x}M2EbGW)Q5Pr`F+B+=5UHdaT'
        ')RHdw1NKKknsw#<Uy}Wobx#vE#cpv1h*brWr69s!JP_d7h=0IE_#6JrAUForf&<{|@CY752ob~}Ac61o`!oLero{-^YlQb?hRBX`'
        'w;$&T=y&XNak@dd1pXQ*WbcLDe=)H?l*TIt%YpL`*;UO{CkOxl'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

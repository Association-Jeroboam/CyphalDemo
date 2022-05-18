# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/node/IOStatistics.0.1.dsdl
#
# Generated at:  2022-05-18 08:39:28.090151 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.node.IOStatistics
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
class IOStatistics_0_1:
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
                 num_emitted:  None | int | _np_.uint64 = None,
                 num_received: None | int | _np_.uint64 = None,
                 num_errored:  None | int | _np_.uint64 = None) -> None:
        """
        uavcan.node.IOStatistics.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param num_emitted:  truncated uint40 num_emitted
        :param num_received: truncated uint40 num_received
        :param num_errored:  truncated uint40 num_errored
        """
        self._num_emitted:  int
        self._num_received: int
        self._num_errored:  int

        self.num_emitted = num_emitted if num_emitted is not None else 0  # type: ignore

        self.num_received = num_received if num_received is not None else 0  # type: ignore

        self.num_errored = num_errored if num_errored is not None else 0  # type: ignore

    @property
    def num_emitted(self) -> int:
        """
        truncated uint40 num_emitted
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_emitted

    @num_emitted.setter
    def num_emitted(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_emitted = x
        else:
            raise ValueError(f'num_emitted: value {x} is not in [0, 1099511627775]')

    @property
    def num_received(self) -> int:
        """
        truncated uint40 num_received
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_received

    @num_received.setter
    def num_received(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_received = x
        else:
            raise ValueError(f'num_received: value {x} is not in [0, 1099511627775]')

    @property
    def num_errored(self) -> int:
        """
        truncated uint40 num_errored
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._num_errored

    @num_errored.setter
    def num_errored(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 1099511627775:
            self._num_errored = x
        else:
            raise ValueError(f'num_errored: value {x} is not in [0, 1099511627775]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.num_emitted, 40)
        _ser_.add_aligned_unsigned(self.num_received, 40)
        _ser_.add_aligned_unsigned(self.num_errored, 40)
        _ser_.pad_to_alignment(8)
        assert 120 <= (_ser_.current_bit_length - _base_offset_) <= 120, \
            'Bad serialization of uavcan.node.IOStatistics.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> IOStatistics_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "num_emitted"
        _f0_ = _des_.fetch_aligned_unsigned(40)
        # Temporary _f1_ holds the value of "num_received"
        _f1_ = _des_.fetch_aligned_unsigned(40)
        # Temporary _f2_ holds the value of "num_errored"
        _f2_ = _des_.fetch_aligned_unsigned(40)
        self = IOStatistics_0_1(
            num_emitted=_f0_,
            num_received=_f1_,
            num_errored=_f2_)
        _des_.pad_to_alignment(8)
        assert 120 <= (_des_.consumed_bit_length - _base_offset_) <= 120, \
            'Bad deserialization of uavcan.node.IOStatistics.0.1'
        assert isinstance(self, IOStatistics_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'num_emitted=%s' % self.num_emitted,
            'num_received=%s' % self.num_received,
            'num_errored=%s' % self.num_errored,
        ])
        return f'uavcan.node.IOStatistics.0.1({_o_0_})'

    _EXTENT_BYTES_ = 15

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8z_5g30{@j&`)gc96i&2B+D(0ww8bjeX$9Rva$8aV0F8+0wn;Sgfgr=&xo3Aq=FVK_v5$gce^3YvC}jM_zt%JN?k1~A1Q(W_'
        'd*?gfd41>XFIWD&v$4{C;@xIexk?q(ft5_j=d4svP;TnRIO!q9SB|_5+y@KKW(}m1^x#GMDfQzT)vU(*Hv$`TrVDK<DE1DHJoD0d'
        '$z6(9=@_h&MklcnH@=>qPtsszu=-nik>Vz0-dkA)4=#O=q?d$qib`?qGYP6X3!_IX<{9-lw#&>LD{JZH7!g}vX(vY-sy*#t1oodf'
        'ZPHSDsz8stNP|qyne(*9)RMRvZyzp*vRSc<cTe*bX0-Zi`ZC3v)On^WW~*hQ<4}sVxT!-;0nI&BDPEzK;VEuE6F~5y1WU}2xWG9$'
        'Hw;S6$Q(;Rd-MseNXYYg7pd41x96ujgT8oEye;l_ZmwrH7C2y(RTB5&&VRUA;QptNE){Ey?OgozxtWlfX^c6)bVRT*5W{(}h$wnF'
        '0+=%HNd-fx(UZ|RmisOIKEaX^ffQcAj4%s?o1k;*`7G;3L5%^jY_`)fK(*ZqT45f<HNfRia+dR%UlM~%b|M|*d?0Qu$&8k>PPjQQ'
        'B5sKH#5-a~JP6qQ3L2~k%MCh?uhOBMLPZ;6J(X43k2k0@!E(S01+-z<+PIN_lq^%cc8CKrJ<M-UP)e&0vB|>Z33;iJDfV_}jbQ3i'
        's7;D*HKA0JW1mJrWq)TP#<5xNCJOEIOr>~hd8&#>#rs7TdGc9tTU0QIu~;lnR{dCVNXO#dxBb<Xm5<3nj>Lh_6(51d$>2olCisUY'
        'c>Kwrj-07^<*|icFyF!3$~s|!s)#m7gF`)3W>WO_hJ=w1AMK#l7luSSB<Hs6SQZw7XQY-&VK=zZ)iy!!1fNfN5Kn&o;3F~vW?e_B'
        '&n{aPx$UeCGG;13XFRd2X+gvr@*J!wdacY_h+7V~1eAGBe<HALEl)0M4%7y%r5+V|97~0je|NDz&ZZZO>i_+m;`L9Yf6_i5;p2RN'
        '#FwdQQY4p=xLI8qY&&-CDaru1Q&#jrgC+LHo^7FZ$}v=&tjF=SLsnH7;yI8w5Km4|kK?UfqqA`Jg_QAH$A}`yTXxCviwoGkX;0$2'
        '%a9n=K5h?YXXpH^)3*NU_tYQs|8OP#12kO%xFJJ{Wv->pixm%SnhzU!x#A3D>mG$^!*u&6v5$-9hc1wM!3M4r&EQb{h+m5rK7&jq'
        'KL7e++bM#k%eGg;`PZ%tW$`!KRRgOe2LJ#'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

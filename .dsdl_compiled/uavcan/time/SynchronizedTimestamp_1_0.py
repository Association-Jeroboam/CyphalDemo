# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/time/SynchronizedTimestamp.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.230578 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.time.SynchronizedTimestamp
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
class SynchronizedTimestamp_1_0:
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
    UNKNOWN: int = 0

    def __init__(self,
                 microsecond: None | int | _np_.uint64 = None) -> None:
        """
        uavcan.time.SynchronizedTimestamp.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param microsecond: truncated uint56 microsecond
        """
        self._microsecond: int

        self.microsecond = microsecond if microsecond is not None else 0  # type: ignore

    @property
    def microsecond(self) -> int:
        """
        truncated uint56 microsecond
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._microsecond

    @microsecond.setter
    def microsecond(self, x: int | _np_.uint64) -> None:
        """Raises ValueError if the value is outside of the permitted range, regardless of the cast mode."""
        x = int(x)
        if 0 <= x <= 72057594037927935:
            self._microsecond = x
        else:
            raise ValueError(f'microsecond: value {x} is not in [0, 72057594037927935]')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.add_aligned_unsigned(self.microsecond, 56)
        _ser_.pad_to_alignment(8)
        assert 56 <= (_ser_.current_bit_length - _base_offset_) <= 56, \
            'Bad serialization of uavcan.time.SynchronizedTimestamp.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> SynchronizedTimestamp_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "microsecond"
        _f0_ = _des_.fetch_aligned_unsigned(56)
        self = SynchronizedTimestamp_1_0(
            microsecond=_f0_)
        _des_.pad_to_alignment(8)
        assert 56 <= (_des_.consumed_bit_length - _base_offset_) <= 56, \
            'Bad deserialization of uavcan.time.SynchronizedTimestamp.1.0'
        assert isinstance(self, SynchronizedTimestamp_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'microsecond=%s' % self.microsecond,
        ])
        return f'uavcan.time.SynchronizedTimestamp.1.0({_o_0_})'

    _EXTENT_BYTES_ = 7

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YYZEqYk5Kd{Eq*o}aQdQ!$?gvULdP|8&iTGAhRYFIvQJWN030B_SxwF;X^<sN3xk^a%14xxDfmHLW_$T}dp4q$H'
        'C57h0#p@Z*jAx$b@vrCp+FD=f{=&6pTDYQ2Qb$(HQa_hjNlBWUsxeM`is7Bd-nO}KE$vSmim&3$7x9<48P2D*tYE+1%1JKk#OsQZ'
        '$J07j*3|kr75mt5URF&E>*<87)25DUC9FM}uV2N%nZe5M@kI<5Q|Z0cS?kHg9})cxbuGMNIDcPLSuE@6rG@k|^<3nejyG0U+Up5C'
        'HV$g1$2Aq-)}F>>Phak0nrWYwRFA!igB=9VrSoZJ3X1AVxVm>7h>s<^usvWC-{`maD26L3ZeADC7AFI}Y%_H}T&#3%jicPuMGWWC'
        '!sPLXf8JVI*;gd$w#vu~GZH7fobXC|q2z=_Bb}o{I9=x?oT*4iixgJcsi^Q-d!cLicb-1!anSibf*PyGFmLLFl3Se@k4<FK(M_S9'
        'C}^b76VZ_E%cd!HE<Hw-2o96C)^eQ15zf>)>S6pMBVp<178A$uku}vax?6yv3nnTQM)sC)M4eM^5Z5)hsIJG@wG)lIb*1Podk?oj'
        'aT8g##8rADYMOAH@G~mS;jF%eefv%yEfI&hK%JCJ)cAF;Cq!Rt{j`1ObZ6l%Gt+vpwY9S?rX;PqB@UI&6`LAN&QB9@SKRrsi+SQK'
        '>TZD@D-KOt7D$8)LbP>FIXNe-E~m2+00g1ETU3j-;TWpriEJaQSEhCB)uo5IXc0n4WJ6#&(&$(1fn$+d?X*i~m)R|W1)cYI?+(Rg'
        'ZM?XD@1_6}YV^_~UoI^`(Kg(#uS7Nlw>V=Xr=^kIj4>#1IOz)CKOU8+xco7koswnA6K1%LOX_#-vlJs*HmV|Q%rNQ~a{wql^$ZK{'
        'fn{rr!3Z?bB@slp6xMf5%{1`~-l+|Bb-sFUu%q5r9}ZTSPwLu?I%@~R!SLbt!>F!@8&Aoa*Hd?R!`!$V&uVj6Co!z1T|qH?bSw&V'
        ')Btd-L8l~P{ZWTcSsvG;`r!huob#@O{r-FndpL7Da%C=SGYT6g<SWglGiBsk2z6O~raoyQC<P%Y=tM<)87`$GeMCjdgGzM~hv9PS'
        'Olxz3p`^5tkc+U!|4N<3aA6N>e6+{AuOLrnK8J89!}7Zd@PJS;oE>W)LvMH5U~2cMGBJG6v>7OzS{k<{XI@Gq4y?|E8<DtcF?{^L'
        ';+=ev+)lV{(X+5^q)IxJ$3l?KsTyBm9DfgI)aML>GcazT1ja%axZR9k&|8AK{?OQG{f-;%M9yw{T~c7it5aM<08_RzHR!}(nFk+A'
        'j}_R4{+bF>SIiSLax;TS(5YiR?$|hikFkB%P_9S%1mf{jJfnnFIV;hk8^?%Qia0LqU;mEb?QgXIuKRvW3pj_fslnqX-W0@5tIS|N'
        '=;{N^Yc7uu!At3lT|P#uX|5myQ5}SL_hi8;`5!0sl&!<IEb$P$ZdLt1;^tuIPnY2(Ze|hUV7<+7&q~+)z+oYec(KNh9MHn`_n0Z*'
        '7ejv7W{maZU$)vW<~;}i00'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
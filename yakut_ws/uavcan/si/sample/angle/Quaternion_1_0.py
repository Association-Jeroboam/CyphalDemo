# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/angle/Quaternion.1.0.dsdl
#
# Generated at:  2022-05-18 08:59:57.979815 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.angle.Quaternion
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.time


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Quaternion_1_0:
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
                 wxyz:      None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.angle.Quaternion.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param wxyz:      saturated float32[4] wxyz
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._wxyz:      _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if wxyz is None:
            self.wxyz = _np_.zeros(4, _np_.float32)
        else:
            if isinstance(wxyz, _np_.ndarray) and wxyz.dtype == _np_.float32 and wxyz.ndim == 1 and wxyz.size == 4:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._wxyz = wxyz
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                wxyz = _np_.array(wxyz, _np_.float32).flatten()
                if not wxyz.size == 4:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'wxyz: invalid array length: not {wxyz.size} == 4')
                self._wxyz = wxyz
            assert isinstance(self._wxyz, _np_.ndarray)
            assert self._wxyz.dtype == _np_.float32  # type: ignore
            assert self._wxyz.ndim == 1
            assert len(self._wxyz) == 4

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
    def wxyz(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[4] wxyz
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._wxyz

    @wxyz.setter
    def wxyz(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 4:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._wxyz = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 4:  # Length cannot be checked before casting and flattening
                raise ValueError(f'wxyz: invalid array length: not {x.size} == 4')
            self._wxyz = x
        assert isinstance(self._wxyz, _np_.ndarray)
        assert self._wxyz.dtype == _np_.float32  # type: ignore
        assert self._wxyz.ndim == 1
        assert len(self._wxyz) == 4

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.wxyz) == 4, 'self.wxyz: saturated float32[4]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.wxyz)
        _ser_.pad_to_alignment(8)
        assert 184 <= (_ser_.current_bit_length - _base_offset_) <= 184, \
            'Bad serialization of uavcan.si.sample.angle.Quaternion.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Quaternion_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "wxyz"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 4)
        assert len(_f1_) == 4, 'saturated float32[4]'
        self = Quaternion_1_0(
            timestamp=_f0_,
            wxyz=_f1_)
        _des_.pad_to_alignment(8)
        assert 184 <= (_des_.consumed_bit_length - _base_offset_) <= 184, \
            'Bad deserialization of uavcan.si.sample.angle.Quaternion.1.0'
        assert isinstance(self, Quaternion_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'wxyz=%s' % _np_.array2string(self.wxyz, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.angle.Quaternion.1.0({_o_0_})'

    _EXTENT_BYTES_ = 23

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8jkSbg0{?YaNpBp-6(%XJLs1(gS(aqE<TxUkh;4Gnp+-)eM4>{+DQm1~NrWtJRCgDr3hXUa)g(uN0sD|Z1R6*K>Hz);{t5aC'
        '1`;Fza`8PEBbQu#%zHi6Go(xj5WhFIysh5*s`|6>zy5n}r23b?o%RA9gpRAZk}Q<Zm=|)#^^+(~v^2cT=N=iA`6g5RaWCcNi*o7n'
        '^3!rLpKxOq!Tj}%?fNWsv~)C!QrOMnF8uvf#tc`nOyV-1c6YhbD2kDM>ep6&QPNR5^5^pNGM{ysF-m%w;kx_-Xn&1ggH>fdu_bvJ'
        '4E<@i0W-`s=%g6y4~mI_dqzgwdDM%2p^{iW<H2JX&;~p%#gv$-JrO6tx;SIE&%e%(RLMvhxeI>GKZ&*M#yt2iHoVK#(Jalno-}UA'
        '<E{}UZG)FS)5eXG0KB}KUwlw2!fnnb%-zQ+OwFIlhh=`=1s~&pso=1pgUo}_W+UmVL~}ohgEAj?gTybN{&#F-<gwr+&LWR1l5CSh'
        't28l!86wy&Cn?jK2Sm%*=R_wFCrp6}#Z-?(@G~|<#<0FxX`BWswd0^PQL+oui_+oF&1w}Un0QR{B_cHm__l<ckd&)smZqWfnSnER'
        '2&(ZjrBKgc3tGxFZ@@tjj}yiJn8De=_HC6!L+yHSe3dd1fn!|VB%1STk)MEGokE~8?!u_rl@MFyima?RAPR79mxUQeFHJ&XzKdys'
        'Kigrl*Y|HQ-`ZG)l#o3cfS=rF;N$y^1|iF&`AKWzXl7wK^ODSvX0zQQJ<gQAN%n;F1x`U<#HQzvJ7i<M(s^hv_?<!RD6*GiVE~4}'
        '0wGx(bDwL?lni@)7oZS`G<x7Iqz$%#w|F8guxdn-X<SvAhv^^#6@-B`P|Wuw<SRB%$HZ4sOYQW7*$kl;q`$m*r$ZLw#E`AKO9Uz*'
        'hFmJJ=Q9OGk)@cgTg2-@lcL3x^}>WzXAB1gWZ+beKdz68MCg7O7Hh%65KkD(4ai}+THZIY&4-DKI1Kb_)C|r6iekZFSzrzn&c<*s'
        '1d^zo5*p!DKE0X5*d}JscVb>#v(k0i7Vn66=?M0dSm?LT)RPYFeEgeEDVFjZzvU`<)pS*FaBi55ojBQxoid+vD~HPbt(p}0ehLML'
        'WOjrSrXN=I$->$n(aL8aWFJR0%x_s4=JU~&5<Syi=J9;~5D&UuuTQZU#iF<@*2HoKgc5Kt3hl&$@*qFuZp(chxOh;m49ZS^*40U-'
        'd=3*KcT)y*kxwCn(kt_s2SDrl4{-Da(9`I9KpY}L9v@3(nKw3jDV)_^9wlXdCCxl&TvzdK7NWf&!$J^~ePV_En5#0sb}YF%tImpp'
        '$tn%f*}N;52B)z7UE84L0UW~LI{k)63j{4-wLt$T3fKUXjCBi5&7fh;UZQrEtB%lzY*uGh8HGwQ;z);qf+WoP98gif&<^|%vMZp+'
        'Agf6P1Q%GtSg&3Jnt+{Z7Or}57uF<dS*P5W+wxGI!v(R!9pqv!gcRMV>tsmX5VU#qcbT93xilYDzaQ~I5$7k|BrS9DIwiUnc?p~k'
        'Wc5CrmnFrIp&OY=)bI+LbbSHsUy9%7rysBYx$!%T1jE@*7KT9oug;3rU&=+=F0=<1dD_=d(&@~DI3pS3wFUy)M_~%DHmDX<N=I?u'
        'NI}Oeo<JNc=(znofjC;wNjpAe$EPjM*zpG9WI<=``jd#$1)W12FX$<|{xsrjLC@IvvxpM~J!kdIBc3bhdBigXy?}VCpcfHO7W56o'
        'MnNyx{cl>km#v*ER?k&y?=8eD1-*uNxu9<&zFAO$c&VV*5#K22JBSwx`aQ%81$`Isd_ljDIA72k)~^M`vjttW{w*P%F6a-epFc#L'
        'E9gz@@3M{8v3|dYI8)FS>;Ed^R6(0Ijy0Q)bsJB0t|tn*VdJ`G^V_!Z-R_?|ec$4bEdJQy2Nr)~@uwDlX7QfIrxu09eT&a6eqr%T'
        'i!UvHW$|l^-&p*%kN2lXt#GLp7Hgqh3-@Z_X)TCa*sq1>weUqPd|3-GYvHR}__`LpsfBN?kiqK?ZUneTklO8-hr|vy&WstpH<$7e'
        'ytsz1%qy>X?JC83@CMvMitqEo9UMCP#GG?^$njlf-@aG#nJu`N&5>1b4HCEpn_}TPcp0%SyofS<gMN@NtgWv!+s(E0jg7T-tJ!Y1'
        'ZnsxgZ>_Aaw%69%>#fy|+s)ScdjFb&rk{Z)Y|4CTdL<nfPsGzcN&HTHa)?XLJ>)4j@_0rXb9Znn6Wv4nLW(L=A^l85@IU^vtocKW'
        'zjp?C9N*jTJ%bdAf5Lq!?x4MYh_m8<;$NBAJP>y~;uqrHqWDn!Qc&@cxGy^Sn1-8evj1@c-woC036SRS1Lf!?B_181`r{+>2h!na'
        'FTeu?Z{+w`3dW2f1H+|<-!{i;bHxrFt-^0Z_-zcoidy`KYaD$Eqc4Y}J4nCZ8O9Vj{|DwyQj^{d000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

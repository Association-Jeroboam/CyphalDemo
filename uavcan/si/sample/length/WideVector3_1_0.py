# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/length/WideVector3.1.0.dsdl
#
# Generated at:  2022-05-06 20:35:08.675661 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.length.WideVector3
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 meter:     None | _NDArray_[_np_.float64] | list[float] = None) -> None:
        """
        uavcan.si.sample.length.WideVector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter:     saturated float64[3] meter
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._meter:     _NDArray_[_np_.float64]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

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
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.meter) == 3, 'self.meter: saturated float64[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter)
        _ser_.pad_to_alignment(8)
        assert 248 <= (_ser_.current_bit_length - _base_offset_) <= 248, \
            'Bad serialization of uavcan.si.sample.length.WideVector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> WideVector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float64, 3)
        assert len(_f1_) == 3, 'saturated float64[3]'
        self = WideVector3_1_0(
            timestamp=_f0_,
            meter=_f1_)
        _des_.pad_to_alignment(8)
        assert 248 <= (_des_.consumed_bit_length - _base_offset_) <= 248, \
            'Bad deserialization of uavcan.si.sample.length.WideVector3.1.0'
        assert isinstance(self, WideVector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter=%s' % _np_.array2string(self.meter, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.length.WideVector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 31

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8e1>&m0{?Ya*>4rs8Mh7I*$spMA%`RdyTy~)m$Yf1rigTcgIE&OC8N1B$M+n0w$5VvMvBxtv;t|Qj>J^TpO8Nxk9~~Ps_kRm'
        '`;zvhuRQkq=AQ9F43hbMbCz#k&i%vDzx?OKME9?LGaH3P7)f41bM8m{bAJ#~$qUjrOAB7owm$x_%&VZRa{6eL(e`<}@@4x)yIfCu'
        'i66uM+m*i+_=!|-sqo_rZbvj3mQ4DThx8K~lxeQD^_;gw^Ma>I%O>jCPXztEbtm14Keb=B^`hsOWzGjxNsIP(!2cDR?Vf7u={uZ8'
        ';hshdUg(#;SE8D1YP`s%>#IV+lE+kfI7$MRrwRX@hL2#OC_(3z&9eDk6Lt)wvs2>w(yR2yavt-NZ-E|5kCTEA6B>S)lype*gMM1{'
        '2E6pfK51PWv<&>B^x`xGEic#S@Ar)GnzROc_izhc^T+l<Tc7nn$0YRga6hAG)c{OejCqi!1r5?9Z0n<5m<H{W|4vOzJYtk2RXm_M'
        'NjJ#8Qw1rRUlQhTQIh#ZK|@mTB%q{7V@muSMC5)xA~Ad>CE*F2?@pG|0x}irz%<SI5Vn`OM5P<uDReLy_yt`dydWXn;NTOI(R|g<'
        'vWN$M2{D%lvI(j@M?Sk(P*PRU1qc)wP?FQ%R}dSxzLBT#9`|B5d>u0qgJLwlK?+K{LqQ6Biwq3q$q-iaEe^JIs_;(w0$2gcZTV3}'
        'QOhzV3Ee_B!G9Z3x;@r!ci%8q!6jrHavAgre9-Z|g#|)ZiTasg9`r06_XlZJ5>>SgGNOK7+#uVG2Mo8MGLmv6kz2&nJD&UQg5DM6'
        'PENMdDhfdmNFbz25*pB=@N*uG#wtJ}5MCC$+Jf8Q8fc3VF+gg`(yG8yop{&|D_}u<kOqwD4hMfFCFC&)a$fL48XL0~K`!uMb?w$V'
        'Sx(ZD+_}9%AQKYsWe)NJKZm5KGW3^41|uj^l$iOWDD}G-L!h7?NS)%3`cRP=)gQv)g85N|5yo^IMs&41J{GY-_Z$^dSQzJMxf=&a'
        'it8n&1^OVz-2?(dz=?&_LLr=}=ho5$%cR_`JGR8G2<ob9v$xng?gZ8oyFM<R*~jbd`p2KHw``@p_G_A_FN^N-4dRC0*i6#xL~839'
        'uT!Y4-{_kH-N_)~u$dib33Cs+{Pd$<A7<3^U~+(~1?=AuH0;-ta*LW3gK9wQrG0(S8;r(H7Ohxj7n#OZD`+So1))$*G;E*MC%g^5'
        'LqiV(<?*mxuTOhLTIB(Sjfi@g5AC9!MTq#It>^DUW8b-ttIwf5O}-0_gQeKXr!wBw3u~hcVs)FwX<J{)ssR+Pm(yVtp}f5g3r5V0'
        '8!OyLU$ym>Lz}ClNV0^^YD;WqOCIwJPzuZ669w8ngCP8EeO&M;fuID;7O4L;hi-sQ#=M21_Mu?Q?KIz9?JA<!C$o!LCloTJWCtn?'
        '7^G1(?g3p3*pmYvj1L*q7<e^}p}~bhFy`wZ1y0bN`Yznn;1--o^VK4w0pH;J@*D=lCY7)k4<c~UwLVYwS~nP7zWm+R$9}=fkGk)N'
        'bT^6XBVL-dHF*`2ViXTjh!1%69>hyD#gCyHeVDp?BWT787?gj@ep{cs?}ykMe{hKTxVv6O5w!o8cbW0$cG<O?VgQ3Y8*^ygxoQA*'
        '#yr8X286$Z#4L_B$QESkPU5|Z#+?#)1aYcykBaYU#L32;5$m&JeNN!KSYJS#Y1~C|{utt1;~qym+PEjg`ICr?jeAP$pGKT++%tmD'
        '65^T0J&Sm%anB*1Xx#IN#~SxF#D&JaAnv~|<X#kVE(t!Dg}gTqFE#EJ#EXslCgSUjOAs$K?p4Is8uu;4^Nss9;<?6s2k~s<{s?iY'
        'ajyxzt|Ojq+-0HP3gXGe{jt#VCy2)z_lD4SRoE*Dz28NgZ(LdEuOQAgt}5)%gg<m)PZ!rCjcW?KEa6{U*yoJn?!G7RrviT_@O^<l'
        '7x;m|n*#3&d?Jtu+!6Rx;8y~_7Wj?8Zv}oQ@OyzT#&~aTQV<t<V!0>mp19i+PkMs&#7<8<?TN2?;_IIHrYFAbiSK&i`<{3qhzeeJ'
        'FcDymU~3m^18nRtapudt_vT7HfrD%Bm3iqEuiZTNNAL!`gDrmCA8z5&!6)W%k46;VW#a97xt_lRbGbZl3dZ0~7=tRi{uH!~{UN-F'
        'Dtv>!|HPP_m{2UoG969PblX%l#js>s(GAtoRn5{AOV%~Rv>aQuWI#hTY+ZL8({OA@v2@F{WxS)BvSrIMJbyIXGG)Vd48t}x)iO=n'
        'vK31)bXmt$%}{jBR&^8D>zb-)s%hH}d@42^wsjBzf3jw1mZ6xAZOR}`kqyf<3`Mn7*)mn#&>dNJWX*Oo6)x+t1;T7Ywskn9X%6s4'
        'X_~5;a7tBGN4FKzuw~mY91WzZ8dwV^g6Xzus<N)=x&_9AvKnY>DYon=j_NqJt*C|!y34Am*t(+XHt;p=Zf-*toQF4k<_EkSweAu2'
        'm^~SH&EK%k_BGct4`@b9et3(X@;33R&xZRN?#-r4oyh$wi{UT%qU{@M!T!F!n^@B^g-0MH75gW=AlNMw_z!lP{g3^tVr$RX?REA`'
        'c6XV5$bQ9K_7S_s*6XPPX8p|g2OALLS4Dkx-;cI~gPT2kh5`;ZF4(2^8+;BPW%x=-4joJAG@MHC5WwGihjR1SraRerzy=T4=z-2~'
        '_HSC?>I+zXvA4R3Bk2dr=q2g@Cjb(-^bP<3'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/sample/acceleration/Vector3.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.473901 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.acceleration.Vector3
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


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Vector3_1_0:
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
                 timestamp:                   None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 meter_per_second_per_second: None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.acceleration.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp:                   uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param meter_per_second_per_second: saturated float32[3] meter_per_second_per_second
        """
        self._timestamp:                   uavcan.time.SynchronizedTimestamp_1_0
        self._meter_per_second_per_second: _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if meter_per_second_per_second is None:
            self.meter_per_second_per_second = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(meter_per_second_per_second, _np_.ndarray) and meter_per_second_per_second.dtype == _np_.float32 and meter_per_second_per_second.ndim == 1 and meter_per_second_per_second.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._meter_per_second_per_second = meter_per_second_per_second
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                meter_per_second_per_second = _np_.array(meter_per_second_per_second, _np_.float32).flatten()
                if not meter_per_second_per_second.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'meter_per_second_per_second: invalid array length: not {meter_per_second_per_second.size} == 3')
                self._meter_per_second_per_second = meter_per_second_per_second
            assert isinstance(self._meter_per_second_per_second, _np_.ndarray)
            assert self._meter_per_second_per_second.dtype == _np_.float32  # type: ignore
            assert self._meter_per_second_per_second.ndim == 1
            assert len(self._meter_per_second_per_second) == 3

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
    def meter_per_second_per_second(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] meter_per_second_per_second
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._meter_per_second_per_second

    @meter_per_second_per_second.setter
    def meter_per_second_per_second(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._meter_per_second_per_second = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'meter_per_second_per_second: invalid array length: not {x.size} == 3')
            self._meter_per_second_per_second = x
        assert isinstance(self._meter_per_second_per_second, _np_.ndarray)
        assert self._meter_per_second_per_second.dtype == _np_.float32  # type: ignore
        assert self._meter_per_second_per_second.ndim == 1
        assert len(self._meter_per_second_per_second) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.meter_per_second_per_second) == 3, 'self.meter_per_second_per_second: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.meter_per_second_per_second)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.acceleration.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "meter_per_second_per_second"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            meter_per_second_per_second=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.acceleration.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'meter_per_second_per_second=%s' % _np_.array2string(self.meter_per_second_per_second, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.acceleration.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YaS#KQ25#}M@qAp6ZEXs1ru|+Zw$GnzWIdKw&3L&Shl_1fI62uwL(cErmu5|a1TmuH;hXf)pKn73;&`<DB@J}!h'
        '7*5{&1M*<xDUW^%QZ?JNyOb#b)K}9-RdrSMSG|8e@%R7D4psk(H?vNt!pLzIlfsL{r=A}%#|_drOO?>f6tj=C%mbZEw$sU&d2W_I'
        'H=misV$4mv80O!}y}iIo93>p(#To4Of`CO#dRnB3^OyxXmFuRMboZE4Fl6{pG4a^S&kY@>Lw_}&n_|ZGw3fopHB;teu<#1sdaFz^'
        'wk=o`_I;XmLr;6IMo0NbcaV=2*Q|?L#LRirNdhj@M10D^9T-p=yf%D-Pt~6AlVF{nvD@cf<wqt(EVS4IKjuD4lxQa`{2<Y+&E(NY'
        '&A7hMZp4zd=7u)G%fM6Gjnfdkyi#0zP%FZ1&KAtw!zm2SU(7>OoOi*;B=lrBsOT{F;b=3l2xO{QkS3uiPPkzjm?!@k85-K*j3jyN'
        'GfC22GO$V!%{@)Hx5r54DaAsfL=rHf(wGrXf(hx#4vFD2(L^M$zFMiBX;f;*L1`*Q8>Sb9!<-w{Dhx33J;j!YP$Xo#0%AfkCYQY|'
        'i$u^Z34&^ZTuRi_+k%#I#ik)q#AigZKjn}c*uE>%xUXIH(pM=XF*wHL4WbyU76mEjRT&&qByAX#djif@xgsj-({KuKZqJKyhF<EF'
        'By11E1pn<u>3-M0-h5+o8A3w#MF@VfzylxOo1P|QnXLV>v3WGIu-x<0T$8o6W`lH?C)EwI&qcs-3hqXtI}W)`Ha9Ar1AD>m9BN0B'
        '{WOn4Fa#C|$&-WyOes%_sMB=;3V{f%dfr0VU>kUg8EJr3&C^`rs>(b}hdHPq9#{j#>_9-g5)E}s0x6VGPWLcd5!8YRmbY%V$YPRe'
        'vVCWXKqVv)O9}P@PeM`T8OG}-@jGxy(PHLxqSUK$42c3la4N@l>Qs>!-EYHU#l0xP3}d;qBeq;E@0!?U{XoSG2D&w>dwGDOSkPD&'
        '7z2s32_%L<5S3%#BAhBFx6%Z!iSFGyKF6<G=^AbFxA@z12=5bL=w6+Pk6N^K|F<o}mx}AZXEJ@+bX9MVH;l&9B;8LOQ;fTnL#BA6'
        'CIxnoLBS!J9ifEDhgE%gQSA?J6jN~I07n(fZ(AAWi{TZ6o+&@~Sur=jgRbA{(kz~0kzeNPd^ra~2^koL>%>BHSe$Zq#Q_UlOq44^'
        '(<;uoD$QlUU?O5}<^f$469|#;O)>QVsQuspjy?x^8h#gugQv*l<4`<sp-eH_7TOfkTb&HDc8A5ODdw}>hb!z#*3Kie+~-=@Fy5tD'
        '(1cMl#noeJ)>(B{91NS$NNjU1_Y}B?MBv)1Y7QYC|7dluK3X7X0qX{sAeF!i7;da!xZWOIUA>>mr_0sdPy;rr>{UjgW;8!?*FZrU'
        '<y|(Y$e?crKDcOexNQ*MGzO{*tzoQOKLt&|Q#Bt~w{Z{Fq;gqhED*b5pyHubJY^2DvL8W+uGbaQCviBme)-!JCx0dMht>BZ)+^^?'
        ')J-!}kXI>Do!CzyKM>V>kS|M*_cQFnsq8nSaW~*V1crZHoPOYi$dW%;#C@D?<xvEU;N@A~_?uaz%~JW$(zC7xLnm_|&KZjY8ypDU'
        '0SXh?<e*wmDILarLnR%tIEpw@(i8T33~{)m<92+)j!#;gvg6Z;<0YN3>rWz1mUI^JL`hHC^`{YMN_xi5pG6!i={c)s4)I(`&m*2G'
        '=>^17CB2AvvZSvePM7qO-T%6^d)eBVw|cHvdv74lm-H&)<&wUM_<BhR;-!*aLwv2IZy{bR>5mXEl=N-H^Cf);ajvA-tzQd>XG^+h'
        '{aZpjUD6+0KYxNaThbfW-(`DV$NK#);#5gjtpBTs6D3`<=UBJ#*s$lR@;X}5O?$4JHoi@JzFXbA)Aua?)Z))9zHjm87Jp&!mlp3@'
        'd}5JXJh1r8;tPvkSp3rBR~Emu_?^Y?yLfMM*b0|wVX+pPwQ#o<p40-bg@amnRtqm`;fq@MvKGFog>P%&yIT0(3OT&<pf^BAL6Wy)'
        'K2kjNo+;gbc`g-0*uwhn&G}cnd!_U`@EY7kvhVW4Z5%rK*qn9Y?Ts%q`wG5NOl?Dl)<;%BLnP1;*Z9IS@G|z=@HWcvHTr(Bu)eXf'
        ')?8cP*xX!iHrATW#;xY+>dlpn)#my}bEC1kd26k)vC(Z<aOtPuF`IdT&>cfZ`D6aOE=l}>y8~Qu?jg&V7RNKvi2D?``kW8&3n{Be'
        '#q<-Nz+d{Asrf_kuUox1&c_U1KQ8EWyWBn?LS*?rp`r5I=*BnvEdMY6SI)N%`JER3HNU&aKj6RNlz+(Y@fN>dj3@zptos`VNO<s9'
        'j4968-!Vr!7~eTWBgY>*>`8;6xB%}IY~0DQ{EXp5dWMdOKY@<b_6d*Za21;-#HNX{sY1g4%@mHlfYBHI(FnQu2g4XY=l?*DoJR=`'
        '000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
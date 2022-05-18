# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/si/sample/magnetic_field_strength/Vector3.1.0.dsdl
#
# Generated at:  2022-05-18 08:39:27.185186 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     uavcan.si.sample.magnetic_field_strength.Vector3
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
                 timestamp: None | uavcan.time.SynchronizedTimestamp_1_0 = None,
                 tesla:     None | _NDArray_[_np_.float32] | list[float] = None) -> None:
        """
        uavcan.si.sample.magnetic_field_strength.Vector3.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param tesla:     saturated float32[3] tesla
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._tesla:     _NDArray_[_np_.float32]

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if tesla is None:
            self.tesla = _np_.zeros(3, _np_.float32)
        else:
            if isinstance(tesla, _np_.ndarray) and tesla.dtype == _np_.float32 and tesla.ndim == 1 and tesla.size == 3:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._tesla = tesla
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                tesla = _np_.array(tesla, _np_.float32).flatten()
                if not tesla.size == 3:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'tesla: invalid array length: not {tesla.size} == 3')
                self._tesla = tesla
            assert isinstance(self._tesla, _np_.ndarray)
            assert self._tesla.dtype == _np_.float32  # type: ignore
            assert self._tesla.ndim == 1
            assert len(self._tesla) == 3

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
    def tesla(self) -> _NDArray_[_np_.float32]:
        """
        saturated float32[3] tesla
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._tesla

    @tesla.setter
    def tesla(self, x: _NDArray_[_np_.float32] | list[float]) -> None:
        if isinstance(x, _np_.ndarray) and x.dtype == _np_.float32 and x.ndim == 1 and x.size == 3:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._tesla = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.float32).flatten()
            if not x.size == 3:  # Length cannot be checked before casting and flattening
                raise ValueError(f'tesla: invalid array length: not {x.size} == 3')
            self._tesla = x
        assert isinstance(self._tesla, _np_.ndarray)
        assert self._tesla.dtype == _np_.float32  # type: ignore
        assert self._tesla.ndim == 1
        assert len(self._tesla) == 3

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.tesla) == 3, 'self.tesla: saturated float32[3]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.tesla)
        _ser_.pad_to_alignment(8)
        assert 152 <= (_ser_.current_bit_length - _base_offset_) <= 152, \
            'Bad serialization of uavcan.si.sample.magnetic_field_strength.Vector3.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Vector3_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "tesla"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.float32, 3)
        assert len(_f1_) == 3, 'saturated float32[3]'
        self = Vector3_1_0(
            timestamp=_f0_,
            tesla=_f1_)
        _des_.pad_to_alignment(8)
        assert 152 <= (_des_.consumed_bit_length - _base_offset_) <= 152, \
            'Bad deserialization of uavcan.si.sample.magnetic_field_strength.Vector3.1.0'
        assert isinstance(self, Vector3_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'tesla=%s' % _np_.array2string(self.tesla, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.si.sample.magnetic_field_strength.Vector3.1.0({_o_0_})'

    _EXTENT_BYTES_ = 19

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8zp#X20{?YaNpBp-6(%Wh7qwBFC0Q;xjz}hAo7+$$Cr+YJA>@=b7PL4*7I$j8i&F*mma1x!W57UsNFV|Yqybd`{RIC6{{#aG'
        'k{o@{#mFT<PCn+np6VG=CIwL6n_Av`^_H)y|9JAR|C<@A{uOU!-B5>-=WDJci{z)Q9dXYO(l|@CG~5<5PmIa~lPmtTn{oTnE_`l3'
        'v-8EMpRgF_mvXifu*B2S(=5(lcg#8oH!|?IB#%O08^x235#Gl<FsWL##e~1Zm6mB@#ZWQ+v6Ej~I!uTDY(KZfw9kxDvYi{Q?eD<Y'
        'F>dx(*<y4PjSbwJ@<V2rZ_sBk(i;?`#ZBj}kumq4bdx}+G?Ab3@F@&v0|&5TTuj!Uh*Mx)oORo0kMko_GL}Z}fFHBZ5-s8U;RlJ~'
        '9j*=sZQ5^3<409IENz090n^5h(-6G8UR-)qE5dEw2FyLgDGbe@>|<M8fM~KLWGXzUXg_bm(WYY=s8sVHO+s6o^usi;&;K(rH1t$('
        'lH_rlE0S)J1FJMKf*B&%4ksDYnukQoB;Z7+F(*uc3B^>G#PBmQL?*DlT4}r~RO-e-X{uxgrst){z1!6)3@~Xk%@>H&B;;EXVnQ;m'
        '7Fm`>GGGRB?h#ZI<VvBQ{uZ>9Yd!^uB5h6-|3ePBf$du=jR)FwKYf)l5`$x0-6opzYEh7aUY)@~WzvCBwIktdl`FEcJ_V-$=XO|>'
        'bM(@rB;h+4CirhFN_Tty_2(Pwix3jBD?{*;2Mm0CZ)%E=MY8fqWBqVsVL5B3xgjen%?9amru1#HD`X&W3fd$wU60%&>uZ(H1AD>m'
        '9BN0A-87FvFa#C|$&-W!Tx+Ie)a|(dg+QdyeQzObunoM$j5NTi5oxY*Rb?Kg!yHr)2G&3^-;)rp#6TUBKuImN*E`Hc1hpW8#f^I{'
        'GM}V|Y~EiWPzeddQh~jIDJY6O!+6~x?JhJaTFh8CN?Da-NEC2`S2_N)P8EsK{SGYFf<+N#7|X2_@x^L+&%_oV1S;k*(5q3?&jS?2'
        'oWZid7$}@gATb1js67jfaJrb-NE2)m)9*VmD{eUHCT)th#XEEe`$^38T4(%Oi?%-cRm+Nn;?}RZN?$i!)f?muqp_W&yNPFuF~4%i'
        '7H`(1!1ppJI3%+}lrZtQs!tZx{)k2~2}cfaRKxtHlVQFXUb5(!Zs%=Y%pTxDzuoOIE}mjuTotQgF$Y2kIT(d@;-TFyP6Oxe@zBRa'
        '`7*Sv;+(J3Tm>8^BJO7l=%N@$h-BLqlaGMq_a5QsOQ5IWcY!!WinKnGNn1>9bTi1+eIBQ_xR&K@Xk1_MP9CAX0mH%}#(KmG`!QCw'
        'xN#)8dduFDhrzN2>1@^)OoLO{{=REayAMhDTdUXbXn~*wtQP41Q~?`ckg;x|sTnk^*-h2<V$~7)fXymrl~Je^BMx;KC`hBc#{m@u'
        '4D7%UAv*$k45FIGKyaZmjP=@1K@+f3&B9d=?!cN<E$WO1a!VelbGRV3xrbcbjvz$0>N*)vHyql${@WI(elE?2)$b>~U&O@;Kh11G'
        'j#Hw$aXW?lKvW+>z8ooj1l`Es)*W0yV}2l@{jK<Iapn;VksH6WNHCmj<xvFm|N5+G{Kd}GW~tk7k!L*(mQLhtIA<&qyw*Tqdnk<K'
        ')dtmqO6f4}8!G9D!xM-jB|YhWk0K72bj*#9yYUH!lWu$pajc}%Zv835iIUDBo-FBUxBd*`bV<*;`E!V)B|Y!-%p#sI=>^2ICB2Av'
        'x}=v7PnGmC;#5hmxczT9yH}l^YfjH~XYWnKYbCvbc(tT&A-+*kf_SB*HxVzF^lijTCH)@a#ge{*c%h`<N1QF`E$7!9;<=K}JO36C'
        '&y@5B&d(nr&Xn}F^LNpm*K>Zqi#S=*CFlP#;&@3{+&NZVJl5QKs=S^k>AE}D9T(rGJKx=2-syV|f8_AT4&Qh96Nf)__%nwO96om_'
        '9PT-M;qaBiFC2d9@GFO3JN(Asw>^9~G3<mZwJ=``&02U+3(spo)WTjZyr_j&weUqPd|3-$)xy`c@J%gz>x3L$cW@)XJ%ZHk#@a~i'
        'aN|sx!FzL|7{ZHd@XEY)%xhOE)`d6VCQ^KlAMWAM;V0&d&m)fSGWYhqUQBMny=)Gxf@_e#HMk<?UVxYQV3#JxH|YDt-0IrWN^@m('
        'ZGC;U*;r{d8+V(_%XgO6mYb_<&9%nz`rVbr+FI|Lf~KE@Cv3(7X}Xr45YNQ(9!dO0d~$$G&OhcEd=ebZNF)9>Ze^l#fL};iMJl4d'
        '7cu-LpV^u}wD^0gAIDL+8G&BJg7_y~nBpE9{D(Lv{ww~Ki;aD8za@Sl9?Xjm#4iOEABu;fRg7r3+QxbxE4H|N%;$<N&bkkl!<UwL'
        'vX9n|K55XG4xauZJV@|{PL8Bxj36>Hn8k0MBenTrn+{juXhJxe7>+6m;@@23=qng~H5lDSI{wZuhRpjvm!$3T{S5#B'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)

# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/si/sample/magnetic_field_strength/Vector3.1.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.424617 UTC
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

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8QiOG40{?YaS#KQ25#}M@qAu#PB+D(w5y?b5=C#zyiIXT)2sv%71c_FZAkMgFrn%kFT$%16xdsfx4+%tI01u!Jpr7EM;GbY1'
        '2$H<{2js!XQy%>kq-wTjmy}5X)K}X_RdpR-_x$O^U;j5dRQ)U7O1psyLdR7+lPr{<GB4zg>nBl~D5<$AW}oOR_jR7}t!~QAOSAa7'
        '`OGX7V{XhMm|x1-j?ZF8Nk_3Lh20VB#9T|?-IhEIT%|J}ceHSxa$hIeswpPj9iAzf#6}Di6Hl%D($HZ#^cVBFDP~-zbtb)Bb7ejT'
        'W5>AJUuBB1O*A%eZ`uu*X0Aq`#Yk^Zj1@Pmw^~NrdD4x2ktMPGlm}Zdpfnu7hzT)Odm>JPb#caSpF7TvG?S6katHjF`zTft&L4ab'
        'Yu@46;h@d9p44tw#lz4Rc<D2x-6#pb%WK8ON3|l{=4`;+1DwLp{MkG<#d(M(ivyMg2Nmt-9vp2Zl75yb?k90ziW6>-_~zMvMuvvA'
        '1SfGGc|0S@HaW0L5iOV|g6(jUGNpJxl#G2&R1$H*GBA;`tV<&J8EYbASYNHw&NM2u<DfLjWCx}fq{E$C)hY}y@tER^L@E;SZ3!_U'
        'DbE@#O+)E34LNrRs`2wILp}X1Xen2G8WKf3PBQ+-9C8EOx3eS~XjlF8Rmw;Nj`8dkQJhzc`~>u>6b>rm4vc0y63$k+A}j0Da0+m4'
        'hlM#uFLgp<zJp<c|F*+qx94AfzPa9jkdR#&fS=rF;NyGK(}Xn0${(8Rha(HinV006tgN(}q{~^RZjoIfeSuTZCb8~1<StoXt8^aN'
        '3x4NNI~mzc@-P5HV1bZ4j=9g3VwnuPJr|%5h}5d@ErboWfw!2ECRo)X$rY}u%)@k$g9^gH8Yt#_65<tWsAJ-1Qc30X4zm$LEl9ty'
        'akott;zX0pdy51rA%<9HV9#e66h)q5ylxY(3r&g^Q`QX=R^=EH1>E3Nj&IeeA`!aZfyGL&FvJXFxphL`sFwFkZ1X{&A`Sz+8rA(g'
        'KvB$VEDMZ5hO;pwhCmRNW1taE6_XoDjBTR(eJAF`bt~PVE%CN^hYn#siTPgZOnlU)?T5c<8?jj2{2kAd*G*UT26@A1Jdcyz*fGVp'
        'TRCKkH)~ShdnptglG!0jn0#E-CktzTM6;NJBl|e2V1CoeFkcKW8T3qfxyOsS13c(@-5%rODHg;Pu__ul5K6$oD6|s~%zkkSICqZ+'
        'E+)#AfoT_KU6tgS&tW3uZpwfziV1{JdZw6q1T4Sz2uEK6Jq^DL#32%-^>HX3Xed*RcBD4N^hP&@tli^LVv4J2?m-K?8SmsFS{`sM'
        'Y#8rRENH^0nd179H0vxoOAdz3Xe72dS1<+cArZK?Rn0!6<8SR=>!SsN7O-xB36czW0mF?I4DHRJb@gtNJ#SRKp$^!rvR4^}n$hA='
        'uYrOj%zJE5k-@+Y{1CDupxYq6Nd#0ESi@MkUILncr)oZ~x^V~ABw0hH+?U((K*hsV@tixz%3cT|x>;AufW+a@`t{$YIQdJdKdgQ~'
        ';r((hM%^Se1vyTM>PB7y`GKfDfP7hcd<cEX;Qk$4M&qt8fC!BExH$cY1;~=$TO>T3ZRcSK7s2bZqWOhcpsiAQaHXd`4TetU9-K3h'
        'F<x*Wusswe@REaSL8WvU_YIYF#NsI8NJ&rF-(!fwB^|fp6Lx&k;*=eqMjS8cj9q^cak8Ydh$l*V%C0|+I8)LycK$5lSV_-WJ#&cX'
        'N_rmgOi3>wo+{}@#FHhxgg9N&%Xa@8*6tN+=c?6n&Dwht@oGu0BVH-#TZnIzlptO%=?%n7C4C$5Vo861c%h{4Af7Mj4-w}|deizf'
        'k9fAE3)a6y#M34Hk@fS(h_fZVW&Lf~^E%e=cM+#bx@7%dMw}?=iap1wjmMfjPnFlvlCIlx-L~;<+4J4$<(<A~@h294YVm!GKePCA'
        'i@&gV-{Lci!s4FA7ZzVx{L<oA7QeRmjm2**e%HeXlfzcHTnh`e(5i*|weYMKL@n&q!i!pXRSRF%!dJEMbuD~T3*XklcUH*Zod<UV'
        '+$c!$cFaSHhr4G=4_=;&#SmU$gZJjuW8S@4#=7tt+(feP@xxslI{et2b$Q6~g=SyD*NUl4xS{o-Rd68^xDZ#w{0s0BpYBrU_!@n`'
        'm|tC6T4}AUuC1@Hwwf!gR`X74dHMFz+Hz}kt+m!%Uca-_TwCj1SkUxS@R&`RFLl?@QSns#wnq}b7w!QrIro^S@NsZ7BaOJvajPf9'
        '0e&H66{(1RB4YSUJ~K6cDDn4pKaOK?M*_WwMe$F#I>lWy_z!Vb{8#)d7aRNHUR(T1++PqMh+hjTJ`@i`TRbdAl!P0r_u*oSOUHb='
        'nBt86csYD+iLHIKcl23<zI5>X7vOP%w{?6ZDPs(glff*0_Z+G16A{wkDj+QgNDBi}#X<a=D;#|Vqpt>|ArkWUhB0W){{f{ABeV$)'
        '000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
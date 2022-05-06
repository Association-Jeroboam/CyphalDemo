# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/reg/udral/physics/dynamics/rotation/PlanarTs.0.1.dsdl
#
# Generated at:  2022-05-06 20:25:55.353820 UTC
# Is deprecated: no
# Fixed port ID: None
# Full name:     reg.udral.physics.dynamics.rotation.PlanarTs
# Version:       0.1
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import reg.udral.physics.dynamics.rotation
import uavcan.time


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class PlanarTs_0_1:
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
                 value:     None | reg.udral.physics.dynamics.rotation.Planar_0_1 = None) -> None:
        """
        reg.udral.physics.dynamics.rotation.PlanarTs.0.1
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param timestamp: uavcan.time.SynchronizedTimestamp.1.0 timestamp
        :param value:     reg.udral.physics.dynamics.rotation.Planar.0.1 value
        """
        self._timestamp: uavcan.time.SynchronizedTimestamp_1_0
        self._value:     reg.udral.physics.dynamics.rotation.Planar_0_1

        if timestamp is None:
            self.timestamp = uavcan.time.SynchronizedTimestamp_1_0()
        elif isinstance(timestamp, uavcan.time.SynchronizedTimestamp_1_0):
            self.timestamp = timestamp
        else:
            raise ValueError(f'timestamp: expected uavcan.time.SynchronizedTimestamp_1_0 '
                             f'got {type(timestamp).__name__}')

        if value is None:
            self.value = reg.udral.physics.dynamics.rotation.Planar_0_1()
        elif isinstance(value, reg.udral.physics.dynamics.rotation.Planar_0_1):
            self.value = value
        else:
            raise ValueError(f'value: expected reg.udral.physics.dynamics.rotation.Planar_0_1 '
                             f'got {type(value).__name__}')

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
    def value(self) -> reg.udral.physics.dynamics.rotation.Planar_0_1:
        """
        reg.udral.physics.dynamics.rotation.Planar.0.1 value
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._value

    @value.setter
    def value(self, x: reg.udral.physics.dynamics.rotation.Planar_0_1) -> None:
        if isinstance(x, reg.udral.physics.dynamics.rotation.Planar_0_1):
            self._value = x
        else:
            raise ValueError(f'value: expected reg.udral.physics.dynamics.rotation.Planar_0_1 got {type(x).__name__}')

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.timestamp._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        self.value._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        _ser_.pad_to_alignment(8)
        assert 184 <= (_ser_.current_bit_length - _base_offset_) <= 184, \
            'Bad serialization of reg.udral.physics.dynamics.rotation.PlanarTs.0.1'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> PlanarTs_0_1:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "timestamp"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.time.SynchronizedTimestamp_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "value"
        _des_.pad_to_alignment(8)
        _f1_ = reg.udral.physics.dynamics.rotation.Planar_0_1._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        self = PlanarTs_0_1(
            timestamp=_f0_,
            value=_f1_)
        _des_.pad_to_alignment(8)
        assert 184 <= (_des_.consumed_bit_length - _base_offset_) <= 184, \
            'Bad deserialization of reg.udral.physics.dynamics.rotation.PlanarTs.0.1'
        assert isinstance(self, PlanarTs_0_1)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'timestamp=%s' % self.timestamp,
            'value=%s' % self.value,
        ])
        return f'reg.udral.physics.dynamics.rotation.PlanarTs.0.1({_o_0_})'

    _EXTENT_BYTES_ = 23

    _MODEL_: _pydsdl_.StructureType = _restore_constant(
        'ABzY8Q-pP50{^{OTaOgS6`lq53M{Obn_+Di4u)OAH0+hZjuXgY0&X*`U~LmCPE*reJ5@v9($zh?V<{0<WDBH@(h{A>zaa8+p7;rt'
        'qA1Cm^O!d$ij;>a5igN)PIvWOc6R_<!Ygf`nyTt^KVO~dd%J$~%R{B?FMh>uS<<pKL$W|nTYN-oHq#8#b9_&Vkfrh7TVW8HVHB{{'
        'me10M>CDIJ&(rC6&~T{(>t_O1*CH#Rw&wGe6sFXy7A)Z)@Io32&(&6J>e66Urtyf;WPyaal$YY+_tf}ds+aVEPt%Xnc(*~rFc7sU'
        'WHS8_1ocs|y(^6euLx#a9o5DRi-yz)QD43zpX7t_@rX7}>T02In0Bk>nmq7a@e#9DVM2z~@l!s`NA&@{gqrX@Af4}5uTS>V!w-Zb'
        'LeT_0Cf{|XsJqO%=7y}!f?kL1Hfka?Z06QOp6V6Q(xfsp9M1wRr{Y5^1tWY-TZXmkxCE{l_$0lV#s>`0(Y0t`bu)Sp)xfmf;O@Ya'
        '%=BC<jdvNAXQsFRv7=O4<&3zIQ)2<~)=1YbNkUFT!fBHcpGwIrB86)*B0Yx@8i0s^1});iPd6mOh5gyiP#Z(0Y95$+fvCgsw9uG#'
        'CfkJ$CN(PA3=xu8Y)ybqh|hvD^?h5Ic}@^yV@5%MeA=&|q)4(c2o$L?60n~|5F2=XE%2NUci9eK#*8?i7z@r2$ym0@^nkDQ!BFAW'
        'VK!(Auq{(XWYWjL3Q(>|?TDe4p+{WSL^r`>&Gy!F{o3n`OJ#5gSr-=Q$xI45zCJcaNSVz2baAQIv#_1kyeK4dbCpHXVl<Fv$T}A$'
        '$0Z*k7q&EVi7YK-JiFcny(7q-fUJ9wZGj+=KuF}e%w$s1K-jHZ1xN%ULfO_9+y<|KwiuB`kQ#C?lDI1q56e~rEC>Z@z?f|a@Ru7x'
        '9uqSVQb;W~X4!^Z5N3J#Qk6`*UP!K7o*|G4F8DG4c_s}YDIy>Jb)M8(P^2i)r!Cu~S&Si2fD2lt_-YX<;-LC<*ep4<ZHzFcTis^m'
        'Y<n(ZjddL5Fqp`5G;GHKlHyc|X@NcnaMgvt5OAW@QYeJ+cx2ggu}s2t-SJ8OvKk%NEBsY{LN8%G@l$!}48L2|t2f@SrhFzo`2h>O'
        '&7!k>gSeqL?z-N(tEKUfktvkMFBPD`Hhf4p1hXDU7`d6{C$$TG_+mT?CYv~maCk+HVLcu=m!f8}7S&ih*@c5ft(BuKS~1O!@_Am4'
        '08lIjLZO_Pl|G2ajWw~sECT~&2rI3|6NdDnz+|vsGsC9<7x6F>Th!8cbOjK8V+Cg)0z3_z1>oQwLi!LS4-`}y@2rb3jmMT-K1A&@'
        'bG$S@=0`OsVFOS<vQcseYvF~V9AbeJdM%A#-WF!HS?!#LZc9T1wn>9i3F;vb7^+m$2M~@wRP)kD2?Qlz-T)GK0pJ3<8#5Tnn?mV^'
        '>t1lToYjWxl9@#>6AC#K@}61)2A&<|Xpn(HM-KepqRye(z`vdYP-iK@n7K6%H~~%-c$`&Z6ZUvPS^CTrYoaUT;i$OFG(_c^4K6xa'
        'WK0Ld!RT=F?=;@?LlM4{{l3N8=^XDgJU@*|KPIx})I5j}c=bBOOTps}s7o4pLFX_UGE5FYkn#`XeJj*Ll-#n3*KoBO*)|*mn^*bb'
        'uhVJ0lE@ky>3+^3)kmTl*y#ut4>%am4IB*PAqUxlO!WbLuaxLJ6y1q*N22dizXy>HB>Iq=A6D}tijJ!JF{DF@zFY0zgLEX(_afbu'
        '=;LbtKBT)7eZN|tKsuP{FDO2fNMA_w14#EL`az`QiGB#_o<u*4bS%-2sP|t~a*rxG#}uC_CGRDq#}fTzq(>9|6{IgFIzf6Q(T^iN'
        'oanD2J(TF*L3%LJPar*z=&vE2O!SjVuTw}T5`9|fH-mIvqMufJei!N9L_eeSEh~F9rT1B+qltb_=|78fIML^n9rMZ`3(B4>t~(Qb'
        'N!fK?`M09%yO76Se_hcx6#br}Zz}qIMSq~^MMbYFdRtMh=!T;A75z-n&lP>7=ogB9spwaVKF;a&kpVS0QVgbxL8Ta6Ee5xX0WSs{'
        '#o&H1_^cRwUJM=;gD;A~m&M?#V(?fEBIxtrY=9F5L0-+(5aQwN84Wv~=S*C}BdpzTb~Uc2pS{J-J6P3AZ|Y#XIBwIl--Ra40ao9b'
        '=P}h@OQA*3WN8$SckPx*?Se&DW8KAJDjvN8%|qDJEyGz&;H;kGr|yFT9a;yD5jM(i#;4{N&dpWk<`<Th<|~VHmCE9U%Ixg<a|^ST'
        '`Gv~D;_T9exy6Nr{4CAfJQPq%z^TM%_@AR1<(B}y{>}d``SJsPxys+-SEu<k{x;Y7JN!DY@*D9EDFCq147gonhNSVn+?3wKi?2RF'
        'uKYdz;~W-$!i_e1TI~_<!b}2~$!&y6?tqal{ClwW$7(w*_Jc%#%fQI)VA)+M(|lXEpWN#9?A<1_JySrV`Sb|<bBoXUzrK;9Cvry{'
        'a8?-VGScPq#=(J7sWA?Z{+{Rm;s5Q}U)YfH$Isu{9bx^QeY%gcscAAB4@j(<Z_(jXTO8ic_Y3Iz^3#2PU^|nZr~ms1%v5Kn`gCIu'
        ')aHL{oIn$X@Ue`K*WeNLF(%##00*U;K^!){ImkgT+krV~z6+p(;?AKCN_%!wamR;ms$J?*2X_t%*C#D~njeg=HtHbUOR!OQx9!K`'
        '(Yzgl4j4aqJegbLeK0)x(f9yH{r3N_kJ}ql@Dh`_a1j<Rwinv_d#4+3wD;eEg*#jK_fD&@c02kB1vRy)puj0`;r}*EXphU*L(erF'
        '1{dg_lKBN@+4|E<W++$sc@{}q#7sP1rBx!<NaSXh(X?G9E>_838^1!Wy(iR0<1O5A1s^|xM?6yW5^3WaPQDF~PWJzPB|C$fa1YK@'
        'z^jqzl`R1mBfOhsw<^EbQyf@l3ot#~gN$P<f!7pxm4c=RKOH!<1@|NTevyB)ab@J-#oi;ZDKcS-1tEp278jPq+~PGEnVe9Wz0~;-'
        '1ql~~f_{y{e6~_*te|JN&-TVA?drG(3-`8GNAI+X=V1Q%pd01*pZG-McPQyE&ltHzf)9*YJW+gL-3Gv(o{L`>TJE%stAKHpjx&DS'
        'cE%%Ec(m0Sz0>Fn?f;C%Ffxu7000'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
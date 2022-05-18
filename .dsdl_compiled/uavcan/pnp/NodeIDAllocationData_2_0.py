# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/pnp/8165.NodeIDAllocationData.2.0.dsdl
#
# Generated at:  2022-05-18 08:39:27.539565 UTC
# Is deprecated: no
# Fixed port ID: 8165
# Full name:     uavcan.pnp.NodeIDAllocationData
# Version:       2.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.node


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class NodeIDAllocationData_2_0:
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
                 node_id:   None | uavcan.node.ID_1_0 = None,
                 unique_id: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None) -> None:
        """
        uavcan.pnp.NodeIDAllocationData.2.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param node_id:   uavcan.node.ID.1.0 node_id
        :param unique_id: saturated uint8[16] unique_id
        """
        self._node_id:   uavcan.node.ID_1_0
        self._unique_id: _NDArray_[_np_.uint8]

        if node_id is None:
            self.node_id = uavcan.node.ID_1_0()
        elif isinstance(node_id, uavcan.node.ID_1_0):
            self.node_id = node_id
        else:
            raise ValueError(f'node_id: expected uavcan.node.ID_1_0 '
                             f'got {type(node_id).__name__}')

        if unique_id is None:
            self.unique_id = _np_.zeros(16, _np_.uint8)
        else:
            if isinstance(unique_id, (bytes, bytearray)) and len(unique_id) == 16:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._unique_id = _np_.frombuffer(unique_id, _np_.uint8)  # type: ignore
            elif isinstance(unique_id, _np_.ndarray) and unique_id.dtype == _np_.uint8 and unique_id.ndim == 1 and unique_id.size == 16:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._unique_id = unique_id
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                unique_id = _np_.array(unique_id, _np_.uint8).flatten()
                if not unique_id.size == 16:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'unique_id: invalid array length: not {unique_id.size} == 16')
                self._unique_id = unique_id
            assert isinstance(self._unique_id, _np_.ndarray)
            assert self._unique_id.dtype == _np_.uint8  # type: ignore
            assert self._unique_id.ndim == 1
            assert len(self._unique_id) == 16

    @property
    def node_id(self) -> uavcan.node.ID_1_0:
        """
        uavcan.node.ID.1.0 node_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._node_id

    @node_id.setter
    def node_id(self, x: uavcan.node.ID_1_0) -> None:
        if isinstance(x, uavcan.node.ID_1_0):
            self._node_id = x
        else:
            raise ValueError(f'node_id: expected uavcan.node.ID_1_0 got {type(x).__name__}')

    @property
    def unique_id(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[16] unique_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 16:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._unique_id = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 16:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._unique_id = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 16:  # Length cannot be checked before casting and flattening
                raise ValueError(f'unique_id: invalid array length: not {x.size} == 16')
            self._unique_id = x
        assert isinstance(self._unique_id, _np_.ndarray)
        assert self._unique_id.dtype == _np_.uint8  # type: ignore
        assert self._unique_id.ndim == 1
        assert len(self._unique_id) == 16

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.node_id._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.unique_id) == 16, 'self.unique_id: saturated uint8[16]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.unique_id)
        _ser_.pad_to_alignment(8)
        assert 144 <= (_ser_.current_bit_length - _base_offset_) <= 144, \
            'Bad serialization of uavcan.pnp.NodeIDAllocationData.2.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> NodeIDAllocationData_2_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "node_id"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.node.ID_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "unique_id"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 16)
        assert len(_f1_) == 16, 'saturated uint8[16]'
        self = NodeIDAllocationData_2_0(
            node_id=_f0_,
            unique_id=_f1_)
        _des_.pad_to_alignment(8)
        assert 144 <= (_des_.consumed_bit_length - _base_offset_) <= 144, \
            'Bad deserialization of uavcan.pnp.NodeIDAllocationData.2.0'
        assert isinstance(self, NodeIDAllocationData_2_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'node_id=%s' % self.node_id,
            'unique_id=%s' % _np_.array2string(self.unique_id, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.pnp.NodeIDAllocationData.2.0({_o_0_})'

    _FIXED_PORT_ID_ = 8165
    _EXTENT_BYTES_ = 48

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant_(
        'ABzY8zp#X20{@*{&5z{9b)TJ;v?EGd>szuUTlCnGdgPwAR+24g*G{t5O7>>5tHo;d5j%3Dx>?<<T{g+E$mwYV2INBm8)zT{xC8i@'
        'qYwE5d@vFpeaYSbKmh*-@iFhK$RfLYBu9``>~6B^)qAhr@AqC6=d=6%?LXezp?{Vy=8MQi$zW)8VN_y%sz!+(49D3l&#Wo+YWc`D'
        'otPP1Mt2suUj1ry@blHrR=wo|LzAYuSj9WbM?NTvYFt)@Zr^hMFjX_?;>AiGk5xLz(|m9<i}dwtSCb?gtI}lYHC3wBa&LI73kx5y'
        'y9*!5^{-Y(yGJ|!vikXI`Or|6Wno5DsqN}h=zELc^<Asw{qGr_M2$4TFoLm$C5jkd;4kA~c~OK*L9oH~YpeL-_~Owy9yWgL(^dSG'
        '-1_XcG4lfTV~%0WCq7KAnWj3ro|by5i?%)<8jegkOmsRe<JHllAkkRaayWyLSMk@DPv3GK;bVh$;I|w26R2V5pI5h6%O{7nRB5D&'
        '$nWSE)d;3>|FKFckl?;yl#N%*omDkb%O^ao4Mz($$In*rVf>;6X(F8$8qA=h)i0M9hZA$6qhX#E<<LZ{o6E<BHmi!Uh943=%oU8a'
        'ynsz&Myut6x4=P8ZsE7Tg1Mdh7K|NdXztzItd_w$i#%4zH9gB#%jffIl$i0b(9<fx@fuUu)$#$h06dR209#+bHn=o+b%45Fl{oPy'
        'hOx3BL7~$Um49r;diBeAu>7xUdSX&-Llxq)hwx-@C)VLiotRlQ3qdI+3Q0Agu^~)YrxA1#W@%W$eHDBvl7&g9VOglu;^f0bEp#ym'
        'KEkJLm}GNZz|ATRFTM6w2r`5!nX84B&L>#`UnI@*b`adw6MQD4F>J2KW@6ag>GoL$otSiz4bWbr1a$C{bFId(FwwI6d9{4_`=<PR'
        '`uqWW6xUjwA7=S#8E)&uE@q<)3;>$E0R{obMOog@b)m|v@YnP>Hn3*mqve-wsVD-ytlbpf!e4JzNur8H_gCnF{qSE`y`x7@?Fd$O'
        '&K<3e_Noy~cV<%beYj93cyR&!AG`wlK01fb?VKL%N_!sLbEil5$>;m!^8?u4cY1UI+uhTnJ^B4XY%iQ11=v1tdh`&s_n#g;EcZWx'
        '?fKKAi}Ku;q`yby`Nvr9qsOIvLfR*#eM;J=rF}-)XQlnJw9iTVytFS!`xR-wD(#EXhSGjb+I?xiF6}p@{VQo-lJ;e3d(s|A`--&R'
        'l(sMJp|k^Oza{Of(q5AGHECa$_6=#jE$w%teN)=Eq<vf3%hFzv_Pf%4Pujnh_HU&9TWNnN?I+U4(w<2B3u%8X?Qf+0t+aoT_K(v3'
        'N!mYidt>jMTs-S8dhX&ackx4a@rk>L-NlK!_=UUpwY&I@yZEiU_=CInqr3Q%yZEzQQ~&|`B!|F(a3|l5?1&=z1&nAIiQ~a1KRUm&'
        'bA3YLWTvfEQ_b-P!wkeVm1gN;mQ^<FnSmbkF(3)PhK2qo2xH|zAD)I=;a}_p0zW)k=qSXHc}CaJ^WoXuL(ogD?({ErNdImC_pJ`2'
        'Ok>|=7^`FWK3#}JIvwkNXv)yWS(QXidU`rG(-^OTnOFnJTZjDcNb4K|Y6!6<!cbiXcz-$1>SyFuh5}1b93%%M(Hy~34R;s!05}XF'
        'cd9@Ph~HUauQ(A1BjU_z)(VJGWU(0`G3p0^u>J%yQXODxHk%>fM2H3II0Lwtf^MZR7~jd&4=ambrWzyzan-Rh39<`;A3?CxmRdy&'
        'am`S3!|;O?O8a7<eM;&Dctb&>PKs>SaR8^9DxU+h=m!<ZmjIwn3SG;G)0t#|mSHa|==q5$Ku-AOi>Z<Ip~kU}4#?j+{g27osMe9@'
        'k@_8l(kxLqFcZdA(A79TV@5%g%~P6Fc;=i2z?D3f_xu)SSrlpk9PB-0NsPc(@vAn)dt|5+JwuwpJoD?)?Mp{{@yqcy<36yp<%7Wc'
        'ay2&P0st_+7XN^5ivKRY;X&-<w}GsbW;0Ol4)5Wkx8jfZ(SN|$v3E+5;~$Sci$8_`ezFx%cRPT3UI2A>3!v@_pzaBvUJyXt6F_~a'
        '1E_l)Kz&dEbyooOq5$fi0P3y)>f-{aj|iad380=AKz&vK^~nyPJ}iK`CxCjN0P2na>Q@9%pA$fRMga9m0o2C?P%jFgJ|uv;CxCjt'
        '0P3y)>MH`MJpt601W>;rfVwY$8VaC(RRHw`0o3ONP@fe*eOdtZNdeTyJAiso0QF%3)Ib1rPXP4+0o3~hP<I7TcTTJLcX;txgDMYJ'
        'seyPVxbpVy&dwd;!T2REimVf<2jLwrtbcIz#=8=XFwF9*M$!wb?%1f%&!v8#%j?K-DO%MO+*YHzdR%fyq-6{_39RK3M;-%`Kp=zI'
        '0dZFkrUQZk=<#KW3u7SRQ+RR?B$Wdl4n#s!X$s-3A1DF<>6Hf+BpKl>6LU`|3mh6hTIg%EAoM}3h|Gi#h|vO3buo`MQFZDQB3lwU'
        'Fk_vl4nEe%c_vWS%C#KTW~zihMt!o#YN{~S<EW+xAc{2xf~R4MkYi#F;e)mz!xaKg+~*(^;Jtp$@;4M!Q;Fa@;aCaIfT}NX(4dXp'
        'E!?CKPhygRA#CdSRg72v89#mZ%jb4>;@?;CYrl+NzwtjW#&5)L_TsnVx8uw4mH4~y_m<}&{a-Ej-@5djZ*Qyu3|{kdzWDo)-+l7G'
        'uLJK%!>ounp8~59p21~CL6MB3LQXav{PZOq1k+<?#uTHTigR36DOdnz#2S&u!DAOW<ZDT?z@9kGtAPsgKy<|{otSBbXfso3h4+$n'
        '5aQ_GD`5=C4UpVN3CFrX?V`&;4_5PP;wJ-@1C_w%Kqzg{h?JLFQ_x(IOw1hT>9dh1XnmP<Bq^|?NQVgwn}idsup)!YDo?5@IB9g4'
        'LuwnabCVX(&T}j7jyfHYl&WKPRh1cd532-t0(djbKZRvX3?pkPFZ>uC44BUdq>2JmZ_`1T#|w-7aFSiCk(Wr%R-grC>HZL?RY(?&'
        'bjd?Gj_IZ*;%6y21SpB2*PkJp>u$EeN679O&^G3t2GepfM@ObP^kOqK<RJW@65~1oDSV^M0uXw?rDncwpZL=Lt@M`rj7~Bt^f7=x'
        '5Fv_<ZaO$KFucM!kft%V;N%P7wZ@|QXzkmu9mYW1lKQpTOkAMQiBThyz$l?z0BfAtE3~rFt)?juMbHDs;4w^PQsHnIeGM(Nm~sGc'
        'fow8?IF}x02{OD9`(32RCL#)(fezq7DyB4c83Z@8V#dn{=o-rH{0ZVb(opLK<(jsUHazR%9JF<n8W3)*b3%#zCf;^47Q5dEZ`aDw'
        '1GY*^vNQD{_OI(S0lVOOc?MJt?AwZUU~P_Jl(ltK&&iANQWz42Swa;ma^chD0GB~}M`=-5fHLqYV$i{Q(grAq7T<3GqkhCCM$WZR'
        '5~9LQ_k-|i*Xd^<ce73i1u|SjXw8=2lf+F|mxCY-55phnBJ;kb(8l6mQ2TuSz-knVkJ#G>+a|J5*i7s#=s7T4=m%Lp{9;xG!5bAa'
        'V7cB;y-cAiRp~9UFJeT3<Pqj>xVGv{j3hFXPF6A@PYJKf3TWw&GngVvbca>Ja{?oPVc>Bym>@)$l*mX3p@ydqjDhN}hczvN`*=0?'
        'g&ir(4-X;5gw%HojtU?S<0V+WB*ol`G2z*6v6fKQO<j^vh1@PNOa#_aN~C*=<cuITagmv5gw?R{AVMb7tN^3V&eV=`Ow>mSnxcS@'
        'KO`BiISB4FNTWJj5jatkRuuPX@ocDgSfQ@%c#c1sLfh`tA%^2Hl(-@WCaQqAf@Ny(O4;48LVz>{PwTAuIrC@6hAXdzZZR)O0&2Di'
        '#OxB50u_dBmd6zB6?ZtxtCD1gbqqdRqQf-yr*OaB0p2sm9s8G#%M(Rbd|kHvWKCzsM$gd+Mj3RcPbd--zIry~CA-az7z#agqe@_o'
        'N%93v39Q?rfm28qlpp#~$6j@*#rvj7He%w!gzwU8Zyh4HFuX+*8r%>71VE~GFGaGgY|tb`J<b94JKgL9_5hGHS^%6FImm_i!r%mv'
        'Fzqw434R>J1)r#G(u|EvTTj6|fch<PsUNh{F)z!hSuG|t#%K6-!dLq%IyJ&luqj;&ftA;)wW3N}<+L@zbr;%y*_7+CtHVtTd9IQe'
        'gMxZGWs&Dd6us)&CO}OicN=C;j&)#{GGy%{VUN=vTxj|P7Eq8el}3V4uhotW{ZJ}*pj`uDx+;+Yxtr}6k_`6&RRT6HVT~oo+^$sx'
        '1<6|2ey7Cg!4w#*wBFb<g=W3=coWI34zVAFXvE<FAP|{hT5emT2aXp|dWUKU4~Jnu;;0&HS{|5Y0Mo^lxgjqdgdaNj0<TJX50^UP'
        '(wcPpT}ar6c%wQYQ&_kpmy-45IcjbMVMFWGa|@TekF&zFce`|p3t&TmlXCGn#9QF3NGdi;q0)eUq>_6inF=I3dhVI6_NPvOX<Jar'
        'yG7KjwysQEjNsKXve;{5K0mfK6-<uEwImLWrM_AdS-P#I6%LOb0!R06a2x;uOlLfk)~IJ2%&*sgCsRGOptqJz3AGbTGm_D!X_jtK'
        '4U95XMU)7!CKRb=BUr92+8Ju#s@Z~S#vj*3pZ~A%nQl&tZ0=x?5vblzfb}vrISmqU&xpPWWMJ@IPvKrLu6Qd?7kZXa;ah0;MrFJF'
        '#p%hK8Du3Y)sVg<i-Udua6Xp(fHogNvVlOynB+hta-5MyoK$rpJQlM<*K_s<Nt;T2QaU9!Y#(|X7bfSx<t5A*I#gZLINU(Nom+b8'
        'FCyl?m+IMlAbq4GWo?D@wk|g~{BO3={pV1~nbnj$0S6uHR!xfox~d>?2V*aSj%sT=(;iEA{o1TMK9GB{x=W^1JDp;(C-Mw}cZv6S'
        'LEj@(==+`ho|!qJ?wIO$a}=?88MEwHLarC4E^!Xl7MNtrZh=Xmh{B84c|Vln2n~Yw^ai;Pq%>%3P>bEo(b!qE?8G##Q&b59s#O#8'
        'utS1d+_}Rqn}NNQt|k*WhXAX1QI-R}y-XyPU4?qXf&`bAyp9AeN64zVU{jhI1U-EAsy~8Pol9FqW_)xlck6lTKmmH-6bJBop;ZLY'
        'ajrOFH06M(?RBycS<V{~eO#VMPzzh(z=?}!<9FaH#r%nUxZWI{X)XJTM7+ls;tE9jGbc)6&P+&XST*E>8(;^g7XudSlw5-cnq^oS'
        'AbO)+pBx`+W;@PW_HG%NOkNwV-(7K~viBU4&9c<M4={G%D)|<RK^9@MQ;-d>cWuWtL5y}dUC4~Z8r_J{040dZ3<+Ewb<5kCTZ~n2'
        'bK=*SqvVpkp+B_A*`}a>(Am5Um<^A?Pf9I}W0sBYg)mnDV$KVEVX0Q{Lb3x$Jx6S#iAy-H8B>dx;ARS>vp>aRP3>JS>mdkZHp2F!'
        '+u#@La*L71+y!gdkjEBI2!B~87?prRpa)W{)ltydVCQ&GL7o>!sqS%s!}k|THrkLt5yy|oT#T&N_o#vm3b8nX0nDK|<ve{ursDR}'
        'u`jN6kUdBl^+4982b^(%*94NZM|CB@!n|l1U|G%Jo-P@sDcjD%9@S-8Jj_n8X2dfjj=LqHkrY2LvfJd+E&&_K$dDR^H?z_ufS>Q1'
        'eJ&HT4re6LNQ$jUX0k~@!{Jg5qb3LdL4>txv4mgX)=O#h7cGEXaV6QpKNc5d<BBTXxatC@&N?>@y)&cZqyl3VgR2;<qIXdesm0VM'
        '>53WkBQ@K`RbHx>RIUuMOWL7n0tv6okt90X!U1r;xlWRr)%b3jCu+>udndW<)KEF>p@&%)Z9#Dm6KEV!WnG-53eHvQ0zJ%;$yS{#'
        '5G3?n>A{t#eg5LjqOM3+IqBc8OE-Bc@<*xk?q79j$YG-^AQH3#i;12T^t?yw>H{V0t$NJnoT{Enr@)7?cS}^|j0&jS-0fmEk5OTN'
        'W=c+CIH?Us3RZPH-PW4%{LaQ1fTk4W$Z5Hrq_>M=T){RqDeyLRF_PgLbrgbzi?cb>>ctuhu8;b3=q%0^AEN36-q~<*DyeQr_XP6O'
        '!$y4q02tyDVmEb_+&`{Gl!2C=_>kv2&gyp1c8#p~%UuJa^Ts5}Er0*qkm!wS=x5ZSQBC+bCkKB?VYWsev6<{S)ES?#S;AwY*Kxw&'
        'NFkrzYE-kuo6rk*P1MOd8KTi#YokNzNS(}wjDu-36#|MH^f%?fIG{Ieu9nn6)zWArkkhz2!<g)#yuVyiB|JlJb2Z)=p($j=3P}X4'
        'PpeD>@wP~)w#syB3J6jQ(AJj}gnYl~Z7jHVyrgUDu3m`Tdv>i-Ks)7;=4R=(s!MJucg-Hu`tj<W%wBBPx%<rU(OL1A#W_Mh{tZy0'
        'xG&ycN6m1NRWD;;s0uu`lHlS}R5PnH2u|}y+S5LYEHnmta#{_}_Jm0*D7RzJ74arj_CFu$o#zE#9O}`n&VVDfQnQuDe2zmJuF86o'
        'xHHzqLnt024Wx`Jg*1G1p;+H>zT&%!|HK)))a+*Moo6shQ1M9~WP$Zjn?_9r^P}w8M6?wT3`E$@RHwRtECqg0Yv;E%>dSch7F!C|'
        'Yv>2S+Ah`hF{6h35hJrZnX=(nslPn|nxP^Fo?pNbaEGR|<WPk+I74?lL!1G=Bonre!ip2vZhWK~3^-Ja8<3wg+b+JF^u3&ncTvzD'
        'tt>0ga(<VkiS28r=sKGl_35;xOYbb|h7Q-xVe#&aw<^6Ie@!ZFbODMC1Z^e-PS8^!u8p46`tx2;5nAm66}<@Noe$_*$+{ygXStt*'
        'AwF$qH${D^o7XY<z1HrCk0g-GLxeasD!I((k_t_=E+*8f$)(E8Zql&StzLo*(iI^5BO0v}%T4g1*MU-s#1@Y<@jmS~xW<DwRI+2R'
        'pX1pl$`66%9rPioZsed85JE38+FrvuU7n1;WA?C+!-3Jk75TlXO5!PkQco9M^w-pVnFaM`EUJMIq|Y}NkKBQ3Upy%VPz90?-WPHf'
        'jSnq2WhfuO1IXTE2s#EUIdX)_9T&qw7v2c0C*_b-;6bp-qTX;#nqGlg=2bE6l+qg#&^<LT8&l4RjvsVfqGQhWQ~erN1nznn1zM*w'
        'TCx`8<Xae5!1@mnn91l~-Q7hAnMljeweI+NjpTmp_rT3DY!rA)5=aM>{1?@{Am?6~lO)Po;wUM;h+%$;y$80MK#VZVGw5^#3ycR)'
        'Zru6M@75jTdnZvAD+cdez1gr?v~z;{`0~bQP1ccS8a@YjeCZ%yfKvD5s0IuZ;xOP35ah;SI81IfWZiNm8Iy8}qzdcK1-@!xV`Q=Q'
        'F#<d{=ZX#ib&M?g&BM{6)Q40kb0HJs+7B3J@l+eFD~J}^43Ev>OChP3^82eY$9ioP_U^dXaJ-XmLZ}N0iWJFTMX4^q;)8V<0qwcU'
        '=*j`NE~&{r+gKMVpUG&yd_pd7a2XZ4>#ezg;K55%1n$dz7FP9Wn|Z8x&B@C+tU^hyxc*0$oG9dJt(_++CDkWa8Jt;9vW|hJ)CCvT'
        'TY&pjsHT?d3I59Il-%kn$~ugqU52rx;scB&($ido6*S^wR8$aSVTe=VN^xdsq-u^<E(oNXL*Zgzd@RSeX~rg3HMFB1@%<iT6sU2q'
        'fh)4Q<d6!4+GAd1B+m6l8I}tYbU#Vrz-j#j2O*+DF*`GXuxR^%l1}H%nMyp1!h2g|RoS|{jxQ4-L(W|VikJ@x;$qo2OA<cb=|CNq'
        '6Be$cWFZQzqdq=~?k7U)6Rv?$S(dZLn#a1c6Mc8)sI$@C?7_7$C#Y?N;fNO)%8OK~;FI$Beh+OWw_|smhYBza!Vg?x-Hb-bkj%zS'
        'IKY*|XJUa<&+-hg3OEEr9XcySr+}PJ8Z8M9NzHVmQ@~*`)0hf3k?AaAlg8{;M6@Bk)@Ms(W2TtlltAI{r)_n;j6ff02Oabf0|aZl'
        'jEk(A#+^+&dBcMC?x@Ch8?M5ugYbQ<4uW*_rV|QznTiCLy1X0@F%SS*C$gJ5m(yNbdjQ|mVpHE1ZQlXI6)q@u0|Q9sOg*Rt{5}Z?'
        'eq|(YmiXH0v6i?!j=U^pzrcWDPog+Rqk}CI8Wov}@QwYhqq$B*A8W~jB&apNS5^#TS#m1c@oN|%)z3EMQH~|nZ#1@EZQt~ICB8JX'
        ';qA(S8?reU#zVRtqV4Yj^*0?j`~3HRoGsrWTeel_=*!1HeE0UdxKl#$&C7~f@7K6`t4qc=y<X#{ch)~wZ(f7{_coo8Yj)n+ORm<+'
        '!4_|`WtQ75o>MO{ISJMrrI17q(-wo<FLIm*dwIRv3-2h^$H`<t=I$kob*+jxZw$hBPjDC8+fRVpuRgFQ<xn}Rv9UBT@1E2osA$Ui'
        'Wp{B|_Zn%-+U+D^Edjyp5VxT{SZ#hW@^*dYzbyIGJHUq&rWBjrm&6w?@$VXd|Kr~d+1T67_{T@*=<Ufz<4@tgpTM}ky9r<Xx3>80'
        'DSUg{eEVbkYX)my^E-C&L-E7$qxiQ&dhyfo@Be~#r0%`|H{AUS{I7lm>TU?1mKTQl1VLzZ<Fj+ir-zaJNtR+5LtX(*_hr*CemOok'
        'I){HXgkCw_sLQ*rK-cu)?jc;Exc=*;;VDeqSMoErk*S{bTIvJCd;Dh|UfuR;>Q4MAOaT?<UNN<#IaYEAzyAA%U-99={{fjj8vVCM'
        '000'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)

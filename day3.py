# ls = []
# print("input: ")
# i = input()
# while i != "exit":
#     ls.append(i)
#     i = input() 
# print(ls)

d_unfiltered = ['BdbzzddChsWrRFbzBrszbhWMLNJHLLLLHZtSLglFNZHLJH', 'nnfMwqpQTMffHlNNLllHnZSS', 'cGpcMwfppfqcjcTCBBzWDsDbDrjzWz', 'LhfjhcdjcGdhFfdGfdjdvwCCZMvvLvWwMLCLSwZC', 'rDnsbmptPmlbQMCrQWQQBZQW', 'gltgVPngDPbptPsbPzVgmDldfTdfczThjJJjfMcJdFHjjH', 'dGlgDflTLLLrRLTLVdQLcQMnbvHbbFzNNvMbnHHn', 'sZjWJJCSjWqfCqSjSmJSbFvCzBMBBzHncHNvMBHN', 'twqqwpZwfrlwRwDGDR', 'zCGGFTQMQrsNRNGZdR', 'cLLQgPDpgcgmvPRHrwBdvrNZ', 'glWpmJWQDcJpQnpjSmbhFtMnqFfCVTCFCFFM', 'zNZWFNZBFrGTdBcZZBdJTrGrmgvppgDHwHmgVHCHCvCPDjzC', 'qtqqPnLSfLwvjvvgvvqH', 'MtbLLLQbRfPRfnbnnLMtnsbdBNsrGWNWcNcTBWZrrcrWcJ', 'sZwstbbDVlHtbhcrhhZLrRpNQN', 'jqGjjFjWnzWGgqWjJJNphnLMRhLhcrhcrSLN', 'qCJzFJdvmHvbtpbb', 'ZSRsvvQvZpsRQGJghClPCwGPChCP', 'FVdMLDdtDRdDcBtmcVFntwgJJTlnNPwJnlTlwlTPgN', 'VqttMWFmDbjbzrSWRQ', 'TsDSBcwshdwSCrgRWZBvgGRG', 'LPVJLqqJbbzpFqwpbvgGRmZPrmZgCvCCfr', 'tzJlJzQllFLqtwHhjNSdtthjDhTN', 'fsDLDDnwvnSdqLSsFSDfsLpbgVttPMpPNjMWVMNfpjgW', 'jhHmBmlrTBBHRPVtMZbppNPPZB', 'JmTTrTmjRTJqSQQSFqQw', 'HPzZFgPFMCHJCcZMcDQGwpLqPLqppwhGvv', 'BrWRqbqRsTSTqNddrVrthLQVwnpwphnvnDnGvGDn', 'tSbBfsRbTfqjJqjCqm', 'pCqrqzmqZzrmCCvCJwJPBRwJBWBmwWBJ', 'VqbqbjFLFfSHnfctBwDdDFTwtRRTDF', 'LVcnbjHLSqHnhbSGGppCMMZMphpNrQ', 'PhTcTPsSPCMvvhhMRPttbNWfNsWFNfWWtpNw', 'rdQrDbJBVVjrBVdLjHHHWNWwfHtzzNtFpZZptppg', 'JJVGGdddjDjDJmdjGqqRSbPMTvcRlqnnMlvT', 'SqGfTrBlSrrrfGGQvCnqZhZmPPhvJh', 'LdVNwgsjdjHmjWwDsDpwsHWtnCnQQQQNnvCnbJZQbNbtZZ', 'DjssDHLLVppDssdLspswFLVjzfFMTfSBcTRcrFSBzBTzmGzr', 'JSJJqlldpJlcdVWMlgMJrcCjrhzHCwTjHrQzwTzZ', 'bBvsGBGNFDNRFNFBRDPsDDHCChhhrZRQQzhjhCjTzWCr', 'FvbLFGDDtWDFBnPGFDWGqJMgJpSdVStllttlppVS', 'clpBdBQBsqGpQbVdqTTWRTSFgLLggffg', 'NzvwmHvZtZZgbDSCLDmfmm', 'jPJjthHzNwPvvjwjNzPzztZBlrccpbVGBQhlGBVlrpnpBs', 'NmFFGlGmzCrNWHvFmFWCFvQPTdDDlbbdgJPtgbbdPDcc', 'RwfBqLwZqffqnPbdDgVQDdtRbT', 'hnptqLMMLwqjMMjzSzHmhvNNrvvhhz', 'hqVrDdPdVDqjsDrjjqsfrrWlctvHJNLfvNcLHNNZRNZHvfZL', 'CSnWQSGBBSnmBnTmSbQbNZZMJNJMccGNHLZNNvNv', 'gFnmBmBnTCpwmBbgWVqjPsrsjplVrjlqPr', 'vgVgJJCphzFjzbwljwww', 'PWmfDgrPrPWlSWqSWlSZ', 'rrTHQTGTPHDDHgPrcrcPmDPhdtGvnvNnttJCdJhtGVnpdM', 'DDDhNgWNLWgDqDgtgtwSngjVSQdf', 'cvFrcGmBrrrCdSfSJQ', 'mBHzFFvFzmsBspsFsZqhqbWlWdPDlLHbqZ', 'TLNpGpRzwGQLLQRTwdvWdWbdbgdBlblb', 'FJDVzZzHfZHVzcHgnvHnvngvvc', 'MzDVSmZPPrqhGmCqQqLR', 'mqHWcBHVcgsbhhnTrrTg', 'fWftGtfJpwJMSdFDLFSGDGFnnNrbrhTNsZnrhTswZZnnsb', 'dSftppdSFStLDpQfLjWHQvWBmmqVjCqcVv', 'frfNzgvzzzJwJqpRcP', 'VdVSnGnHqhDDTdqhdLWmjMTmjMPjPmTsmsmjmR', 'BdGLSWtBSWDtVqdSDVGqtSSHFZFZtQbZlZfNgFffrgNrvgrl', 'jBVSjsJcLcqqjtgcmRFRNFFzFm', 'CnHnWQQGGWnnCnfvCTmZRZgNtfZtNDZPtNDtzl', 'mWWGGdmQQWwrHHMBBBhrBVqshBLBSL', 'cLtFcllvrslGLcLHVzDZQzzpznWzQtQZ', 'TmShfSSPJRRBBfSgmdfBJhDNVpGzVZpzQgZgbWzpnDGp', 'BhJPfSqdhqJRdBdPqTJBChvrFlHvvCGCccHsMscvrHvv', 'zfddZTpZLzLDfLtDCttdTfZPnlcPcnhjPDnlcjMchDPjnP', 'MQsFvFHJsQvmNvvswljgbPbwlwjnmcch', 'VFVqvqFQHqVJRVCBLpqTGMzCqtMZ', 'PZdVgNdQQcdcZQtGhnHtBlvlvWTnbBHWWH', 'CDJmzqFmMmLfqmzFwqfzfwMRvpRbTWBBWDnlnbnWnTNTnB', 'zFfffjCqwLJCfrCFjCLCzCMsjSZjQNPhQGVSQQZhsGjGgd', 'nbHntnqPQwTHwQVC', 'BzfSZSpcBZpzpPhSBjRTCBWTTRWTTTWR', 'pvZpzPzNfhddJGmmNnJb', 'GwTgWlvbgTwMrbwTrlWvwtHBNtNvBhBtdZcShHDtNS', 'PnndmnCmnJFnsmRdmFnnZDhRRScRQQHDtDNtcDQS', 'CLffLsmqqpJljVdlpMpWlr', 'dPCzBLTSLqmqdSCsmrTDVQjZfjfVVZnZhhhLGQ', 'wwFpgvPJNwgPPwvZGnQhbZQQFfQZbf', 'WvRwwJpHHgpNMNqdTdCdqrmHBPtm', 'DbWwjSGFSFfwGfCwDSSPPjLhgrrLWRJRgggJphLzpJLq', 'lQTnMHdcQBvlHMMZBcHHTrbzpdzgqrpLdqzzVRVRVV', 'vlvlNlBQvBZTQBnHnQTTBBPwPNCCsfSFmbSFfmGPwFmj', 'hGGQtbVjhRqlmqqrmDlpmw', 'gPMZsMgdssCPPsvrgZcTZTPSnnLLnBWDwLmwWwBnmWSnWNWB', 'TsvgMPdcgCfMdcsZJRQhVfVRVQFFQGtr', 'NfpFTTpFNbpZMRFrJMMMCv', 'dWJPngDWBtPVBdPVGHZzCGHZrrvZRSMSzv', 'WDDDVDPlWnLBVgnsgJmQJNqThNmbjlqbbh', 'vnznqvfrzzVzrvvnfVqztBtGbMCdGmCcdccJccCLCcpSSgcL', 'RQsDsljDlhssWshHhlhsHTlLbgJLpmgbbcMSpSSbcSJgjd', 'WswhhHWlRTsQDwWHTRhsvNVvwqzfVmNBtZNmnzzq', 'cjcPfLlQtPsZQlfHZJqVSFdVwmSRRqSSddwDvF', 'MgNbBgzgnwdPRFmSPn', 'CMGbNNMhCMzzPzBpTNPGBclLcLfsptHQfQlZssLcLf', 'slsdfpSlllpTVJJGgGDgHMdV', 'wrBQrbQrhQcpbQrhLwRBrjVVgGGPgZMtZMVhgMPMGHPg', 'QQwRnrwRbbRcmQmrjRnjpvNsNTNSlTmsTqCSvsNSWz', 'GWNwppdHdpmzgPFPCRmlCBPB', 'bSrJhJSsMhrJMDPRCPBlwVCtVSLV', 'QbsbwqQZvrJhhQrhZZrhchTfnTWGNvWpNnjHGvGjNdGT', 'NMZGmnMBWmwmNnGwHrHvHzfrvrVVVj', 'pSbDRLgbpJDPpRZRQjjFqVhhDFjDVqfrzv', 'sQQscLTZcsTpRsBnmlBcdCMBMtlc', 'hwWslbGWbRvLZvcscZ', 'gQnmmrNTmSnTfgwDwVwpJvJPJzLqLJTLLvRcZz', 'mrmnSrDNNQSmmwdggrrDbHMGhtdtGhGlhtClMGhM', 'qQdlGcvDQDQvDdmtPmmmlStbjSrm', 'CpNhzWTCTRznBMvwtTjMrHtSvj', 'nWzsfZCsBhNpZLgGdQDddvqd', 'ggjTjJWDVVVRTwQcZWvchshWhs', 'LmFfLfSmBtCttNLfCFBPFNBvvvhrcQdvsrsdSwdqcwrwSw', 'CHttltmlPLMHRTgJQDgRDTMb', 'RPJgCdhgPPSzvWDcCfGHDcvf', 'HbrrwBspTwWDDnqbZjjD', 'rQrFsrsstQMQHJdHQm', 'GVwQVGBZBNQwsjdNcMMlgJNPgj', 'SWFfSzTCSWFCSpgnJLSjpMdc', 'FhTbvrzrMrDCVHsVsHGBtHwv', 'FsqjjVzFVWFqRRWBssdpNSBHwJpHHJJdddSN', 'lQgmhvbTcgTgfhTQhSCFCGJHSlwNtJdGHG', 'vgZPbbfMhbTmchhjRFRnsDRPWVqzWz', 'cvwfjjcJjqhctvSpCgCFVhrFCrpC', 'mRsQmsMlNNzznWQlRnsMRQlSCpLNbpwSSSrwFLDFLLLgFp', 'zznlnGlmRmMlPZnGQzMszMRfccTjcBJjtJtJjqTZtfwBTt', 'PtCwCCVqbjNNqqvGssPmHGsHMfPH', 'dcddcWFDJJJcLczhWQdcDScZvHZgpGfsvMfSmsggSvvnvM', 'TTQmTDhdQQzdRwjBVrRwCwBbBr', 'BnBsFHCrcnBrMBPSmMSCmrcFqnZLddLhdhdGLvqLqgqnLJJp', 'WfjTlNVDTtjzNWTlVMWNlTwTJphdgpvJLGLdgghZvGLpwddq', 'zVjbVblVDlNTlbzTzDjllDTzHmHCsmcMHcSBrCBbrHBcBPSC', 'ddlcGQlCjQNGQmPLslZTlmTtfT', 'MDzMwSwqpzpDRpWRJwgZhttrZmTPfZmrmtrMZZ', 'JSqRBpJzwgDDpqDqvpBRdCjbCjQCFCbHvdGPjdHQ', 'bwzPwGLZMsbJMPPLGLMQzbhhQRvWWtVqVhgCVtWWQDqt', 'HddrHFnFNpVnVLhnvLRV', 'NLdrFjHTBrrdjFSpFmNBmSfZMwZMJJfSffbwzwPbczbJ', 'QTWSzTTLwTfwflSNJRdvGlRGcNgJBl', 'FnmmqrqbBBgRbHGc', 'MFZqrCVCqmZCprspFZmnnMsDfzWzDwSfjSwPQPTLhffwBLwj', 'npfgFRTZRRnDZLdgRfRrrjcWzGpWGGGQrjjWpP', 'vblVbvSShhVzHWjzzlrPWG', 'bVwqvCBtShqBhCCtqhNqCJRTTBDFJJLnJgDRWFBnWg', 'nHDNQvgvnNZHDnsGcjfNTrTfVrfL', 'SRWFSBRLtSFqjTrVVcsVjTSG', 'BdBbRttWBdbdWdbppmZlLmgwHvgQvgLZ', 'PQRZlpDDptQSclBMGVBdhVFGBMpf', 'nnrsTCWjLJsnsSMShhGJfwffwV', 'vjzqsjqgSHbbtvHZ', 'DgFmbdSDZbPgLbDDmFwZwgLSfccGcGvnvvngsGGnsGMNWsWs', 'HqztHHhHVhHjhRRhJtCVBCfNprMWpcMMJfsvvMsGscpG', 'tjVtBVTBtHHqCRqtzQwTPSNdSwPTTbPFDdml', 'sbmBmHZbRRRmwBmsSjHzRjmSCNFLNLLQNQhFgtQLzNztlrff', 'MpqPPDPVnGqrJpcqqJpMVlgtlLFLChCgChCCQgCtCD', 'VdcVVJvdrVWHbwHWBSSBRb', 'tPDVBzzNSNdDSQpMQMTQJMMQMN', 'LqSWSmbsmfQTTGZMWGCW', 'cLjLcbrjqmvfqLbfmqLwDBBzSHPzlwzcdBlnnP', 'SbnHrGHSrrhHJBrrScDfcPDMfpPGcGcpDL', 'QTpmpmmQWlZsTvVQDMgggFLgFcPf', 'zsCNlltCslzlTNsNlShwdJCpSqdHrBhpwr', 'JZmFrmLGjFZdDGrrVTvzmPVvRRVzwzzl', 'WBnfMDBqMsgDBqpBvzwVlCwRTRRPpvlw', 'WfghfttggfSnnqbDftfqSBBDQdHhZFFJrrHFjGJdGjFrjQLj', 'rNLRjrlVlrFRJzlsjrVlRFGCmnMtftgCNDDgDmCfqNgPNM', 'SpdBpdHbpHWhZqnCdtCGggqCPn', 'QHHvvWwWhwVVQRscVzGl', 'QffLtMQGMQfDMMwMTJwqWHvH', 'nSSFznjFcfjTgVJTJjvT', 'RrBpcfSNpRBcFshrCtQrDGLPQb', 'GctcMldStGwPPbcLsQTV', 'jhnzDgnHnnfPVwHQTTLTds', 'gBgzDDhzvqdGGvrtdvtm', 'PPwRWVTvRvPVLwRpMlzmbmsbHWjbbs', 'dFTFCNfdjzjFjsMF', 'SgdffSTrnnqCgdqgcNrfSZqVvVLRDPJZQwJBLPQPtLZwJJ', 'HSzDQftHphTBHFhr', 'WMmJsMJNLWNPmmsncjMJcjtvwggVvhFFFhjrVwrjrjppvT', 'WWPsJJCWCtZZZRGC', 'SfFZQDRLgpLlRgQRRRFWTsbhBhgTjbWBjhshgw', 'tHVNGjtzzHvMMJJhrWJNrTrPbP', 'jvVVvGCGtCmjHtdHzQQfDpSSlDRnFfQFmR', 'ZBBPfVVPPrVmrWZJzNdPznbnbSzznP', 'gvgpGqFFMgMcGgwLwGpcJNZSTZbdbdzNNSlqbTnn', 'ssZLgsMLQvcFpVrhCsmtWHjrrW', 'nFvhRnWWzBRPHQqcqqCqmFbd', 'SJDJgVprLfDfbJmHmWWHQtJW', 'wVsgWVSTgLjfSsVjVBRvRNwwGGRhNZhRMZ', 'wTRrRBCTPTBPlgMqgHCqggHLgg', 'dmDzpQpBdmWmWzzzDFzjGNMSWLSgLVGGLVNSLgSg', 'JbFdmQQJpjpptQbdJJmDmdtnZhZRflTlnTrTlrhBwPPc', 'jwSwssQbwbStlhRgtsVstn', 'zPzFdFFZccPDgntzVHHgghRz', 'vVVdfFmZPDMWZZBmGQbwJJGCLwwMwJCS', 'PLLffLFqqNLwSffbnVzzRf', 'lsmgTggChrgDtZsZVblMVJMznVnwMBnb', 'hDZZTmZvhTgstvwNFdqpWQcqvP', 'mmWwpwqtmmHTqHpprRZQPPZLZWSFRFRB', 'gzcgscgbfvhRRNZQRRQPvr', 'JsjhcshCfJgrrpttTCTplH', 'TvNrvNrJfWWvtJLTHhvZZhQQwVGZZhbV', 'mFCPmBMPlPsPPBsMFPszbHQJwwHHhbZVQVzjhGHZ', 'qmlBsdCSmJBmsBBMnMMTDWDNcLrDprSNcWDNrW', 'HSnHCVqTddFHSVqFqdStSQGQwRzQCzCRzGRRGNPQwz', 'jhlBpgNvlfZjlfvmpgfgfBrMRRwMMPPLQMZRPMWMMZPQ', 'hflfpgjfBfDcpchlpvndbHFDdHqSqNVqNVdn', 'QBfhlVNfHSZHfVCVHSQfZfTCctdvdDTRtjDCtTRsjsvj', 'brrWWqzFWzwWbswDchhTRtDhjT', 'gbrFLnpzqrWPgqpLWrhnHGZlSfLfHfQBGVfHHNVG', 'hcFmVScmQBVhtcvfHLfvHSnbHRLn', 'lzQqlDqgpWPvJfRnlNJvww', 'PjCCCPgDgqGzmMtCQstZmBFs', 'GrnrHrmVVFMFhSSbSfhR', 'zjTqLtBjjdWdWTLshMZMDbPNRMSSqSPNfD', 'dTWjdtwWhjWTBzcnrpcwmQpCwcpw', 'BgtVBsgVVJhgGsSGJbghJqbsjLfZmLjmmtfZndNNZFFZNLdm', 'MHTlzlwHSvPvzMSPCTMQCNZdjjmnfQjdZfNLjF', 'HMDTwPDpzrTzpScBghDbVqRBgRBJsR', 'qjCsTmrrnnCmhcFrCjqmThRlbHGvJGvvvbRbbJRcQJRG', 'fVBBTfMdSZLNZgPdgglGRdbtbtJRllJWJtWb', 'TSZZSpNMPBLgpZLVgppBDFhzDmjrnzhjssFqDhzFnn', 'MDtDMWmMQmdzmMMqvlGfRcjzgpcPPjczPl', 'sZsHJWNJFJNbWFBhFBnnbVclbVVPglfcRggffGGpjl', 'srHWLNZZJdSLSdvDMw', 'BFqsPnsZcgnncggccqsqqpDPtDWPpPNTNSNThrWtSj', 'dQbfQQJJdwdmFRbJLRJdMrfDWrjpDrrprhDDDDNWWD', 'QGwdJmCFJZvGsvvncB', 'GRRNSjrffGTSPrNTffSgcJTwWJZbbZvwvwtVwWVJZv', 'CMcFsqmBQzMzshsBQBQvLWmJVwZtpJLJwJLvwt', 'qBzChnQlzMcRSnnRRjHGGg', 'dPPbPWNdTBbDpHPHpNsgzvFlglvHzvSFzCFF', 'fntqhGhRMhnnnGGCVMRhCVlSjswFvvjzjSzvQVSgsl', 'MMqqJJRCnMhZLCRhtPNrpZPDDWTDTrNBmD', 'VjVGNTNlNchVjNGRWrSWWtZtRrzncR', 'BTbbbwDmCDLTbDwfHmzZMmRrWtzPrZSZtrrz', 'qDLLqvwLBsfBbBdQFQTJhqThVTQJ', 'qBqPBGZflhrWznzZZdsnzv', 'FmHRcCCsCDwDbjtzdjWbdz', 'cTRwCCNHFNmwRgmFTNCFTJqqfqPJsPhPBlsrsfGf', 'JTNhhNrCTcWpJJcpWw', 'LLdLsfMsdStbtggLbnTpwfWDzpjvnnjzcz', 'MqSZsgbMbGFbZtgTSZSFSLhhmHlBQlmrmrPHHCPPZPBr', 'GgjjgpGvpJJtjgvPrJttsLjVwCsQsQNLsfLfMVCl', 'RddqZqzcZdSWcHdcqQfQLMwVflfNQNMQ', 'FncWTRcFlHWFmcFTgPJhGvDgpnnhhGtG', 'ZGPFJsPQCbZCCbgz', 'nrvrnGWTwwqTBRcpCRRg', 'DnGWDldNmSLSMdMQ', 'ScDmPPPmjmjjWgtdSmdmCnNqVQVVrNRTZTQTQDHHZGNH', 'wbbMhLvMJpRwJQrJGHqQGrQHqr', 'wzhspwpppswsMFLmtnzjdcmdPRWPtS', 'fPlLTtBlTjDbWcTMJcncWqss', 'LdvLrLpCRRQQmvhhVNpwRMWJZcFMZWJwJFFFwZsGcs', 'prrRVpvvRVNmRvvzHjHPlzPLSffbbPHS', 'bbCbzsQbBzbBFbFzFfJHfVJPfVPtzZttpm', 'hwvrjDDwjcDcvdnNvwdnwwDPpNtNMVtPpJpRmVMPfmtVZR', 'mmqDWjhcqhwvDDdTsSGGCbQGSBBLTGGl', 'wthtwrBQhhSrqJJVLMRPPtJLPF', 'vbmbZqfqgsfHmcllmLLJNLJMNFJNNvPGJn', 'jHlDscllClCCgbZzhWqBzBQzprWCqS', 'DwpDlwDwllhJwbDFNDwFPhDnQnZZzVVnnBrtNznzSSzZrr', 'MHPfWRTgWzTQmSTTZt', 'GdPjHLRMCfcGvwqDGbFq', 'NGdNpDPdNGLppLpwSNFFFDLwnnZbMnrHlHZQcHbcnHQcPcQM', 'jBgBsjssgjWJVGhBfhvJVnMlbnZQVrrrlHCcCZrl', 'sRBgvRffhhtvtBgvjgttWBJTLmFLLwdwzFdqLDDDqFGdLFTd', 'RBzRGRGBgnrPJrRGGWWbDggZTSTVZVFFSVZZdw', 'tfmLhjfshNNsqpppfjHdwVdQZbVbQFVVTmSVDV', 'jvqtwHqCNLNsNhNfjssLCzGJWcBRJRBCBBBrrWnGrG', 'cGDBdNFdNdDStNtGdGQGscDMvZjjZWMvMLjsjjLZjLsJLv', 'fbRnRzHVPClfRlbbmfHRlPvZvMLpqjvZJqZMpzMpZjBZ', 'gfbfBgCHCPVNhNGgTtFDcF', 'ljjvLZvvllFnlLJLJjLWFQrVssFpsGMFpNMGsr', 'qbHSqHTcHChqCmTSRqqBVpVdBQsVQQGHdMprWV', 'DbtcCqRhhTRmDnPMlLgfgztlZZ', 'QtMQzPZcbtGgTtLvtf', 'HwcDsdVVDnNSGLhwvffJvfTT', 'CSsdSHNmSDHcCqqcrrzQcC', 'nDNDfmMnmDJRNfJJdMDRBdwjcTtsSHvBTswTjwLtsCts', 'QcbQrZZggGWVVWbZZjStswCSCCttGCwLvC', 'ZgZgbzVglVbchVVrVhFWWpnnpNJmJMqDfMJnMRqNDDMD', 'WMfNvsjWGjsqFjqTRRQVJztDzVmJHbft', 'ZPhplcrLrmzQGzmz', 'ZPddLPlcSclhZChndMvgTjjWNGWMGWBj', 'nDLjMchghDcljfjffpfsqTmGCTGszGZVVzHV', 'wdFJPFrQRwSNbjVQCTGsHZHmHCHs', 'BRJJSddvdBrJwrBRNRFRSPRjvclLpWhpglgWpLplltnMgh', 'BbVRzMcpbMNMHMTJmWdljdlJjT', 'GtsqFnfvGSFqGfQvgnWWZlLlLjZWtWldPmlT', 'sSsFqsqsGghwQQmfGRHbbVczbwwBpBpHcw', 'BBFCBJCsGJBBgvgsvTlVhgNg', 'ZnLdjRQddLRnZrlScHRVTTSHhRvg', 'fnnjZLWdrnqdWrrPLddqVqBzGDJJFGCBDfJmbDzFMbmB']
# d_unfiltered = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']

#Part 1
sum = 0    
for d in d_unfiltered:
    mid = int(len(d)/2)
    c1 = d[:mid]
    c2 = d[mid:]
    char = list(set(c1) & set(c2))[0]

    if char.isupper():
        priority = ord(char) - 65 + 27
    else:
        priority = ord(char) - 97 + 1
    sum += priority
print(sum)

#Part 2
sum = 0
for i in range(0, len(d_unfiltered), 3):
    d1 = d_unfiltered[i]
    d2 = d_unfiltered[i+1]
    d3 = d_unfiltered[i+2]
    char = list(set(d1) & set(d2) & set(d3))[0]
    
    if char.isupper():
        priority = ord(char) - 65 + 27
    else:
        priority = ord(char) - 97 + 1
    sum += priority
print(sum)
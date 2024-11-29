最新環境　FFT (swapテストは古いです shとかあって使い勝手がわるい)

## 更新の必要があるもの
info.json (作りたいsol genに合わせて更新)
test_out_maker test_case_maker (info.jsonと合わせて変更してください)  
いつかはjsonの設定だけで作れるようにしたい(理論上できるはず

# in
 テストケース (/in/{generater_name}/{generater_status}/{case_number}.in
# out
 実行結果 (/out/{sol}/{sol_status}/ {input_file path}.out}
 quantum　は　アルゴリズムとしてだしたい値、量子状態を入れる
# err
 工事中


## json について
  jsonに変換するときnumpyやcomplexはうまく行かないので変換が必要 -> 変換用class（工事中  
  変換は *solの方でjsonを受取,jsonに保存できるようにしてreturnすること*。test_out_makerでは計算結果(dict)の加工をしない。
  
  



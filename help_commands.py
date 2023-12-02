#helpコマンド 全体
commands_description = {
    'test': 'テストコマンド',
    'help': 'helpコマンド',
    'hello': '社会不適合者による残念な挨拶',
    'invite': 'botの招待リンク',
    'add': 'たし算',
    'sub': 'ひき算',
    'mul': 'かけ算',
    'div': 'わり算',
    'mod': '剰余',
    'exp': '累乗',
    'log': '対数',
    'root': '平方根と累乗根',
    'sin': '正弦(sin)',
    'cos': '余弦(cos)',
    'tan': '正接(tan)',
    'sigma': '数列Σの計算',
    'poll': '投票コマンド'
}

#コマンドの説明
detailed_commands_description = {
    'test': '引数strに入力されたものを返す。',
    'help': 'helpコマンド',
    'hello': 'ユーザーに挨拶を返す。',
    'invite': 'このbotの招待リンク',
    'add': 'たし算するコマンド。引数は最低2つ、最高で5つ',
    'sub': 'ひき算するコマンド。引数は最低2つ、最高で5つ',
    'mul': 'かけ算するコマンド。引数は最低2つ、最高で5つ',
    'div': 'わり算するコマンド。引数は最低2つ、最高で5つ',
    'mod': '剰余を計算するコマンド。引数は最低2つ、最高で5つ',
    'exp': '指数を計算するコマンド。modeが自然対数の底eの場合e^exponentを計算する。modeが他の実数の場合base^exponentを計算する。引数baseは基数、引数exponentは指数。',
    'log': '対数の計算をするコマンド。自然対数・常用対数・二進対数の計算が可能。引数valueは対数を取る値。',
    'root': '平方根or累乗根の計算をするコマンド。modeで平方根or累乗根を選択。平方根の場合引数valueに平方根を取る値を入力、累乗根の場合引数valueに平方根を取る値を入力し引数radicalに累乗根の次数を入力。',
    'sin': 'sinの計算。modeで三角関数か逆三角関数を選択できる。引数valueに値を入力',
    'cos': 'cosの計算。modeで三角関数か逆三角関数を選択できる。引数valueに値を入力',
    'tan': 'tanの計算。modeで三角関数か逆三角関数を選択できる。引数valueに値を入力',
    'sigma': '数列Σの計算。引数kに下限値、引数nに上限値、引数sequenceに一般項を入力、一般項はk,k*2,k+5,k^2のように入力',
    'poll': '投票コマンド。タイトル、説明文（任意）、重複投票可能か、選択肢（1～10をカンマ区切り）を入力'
}
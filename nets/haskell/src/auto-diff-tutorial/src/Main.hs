module Main where

type Model p a b = forall z. Reifies z W
  => Bvar z p
  -> Bvar z a
  -> Bvar z b

main :: IO ()
main = do
  putStrLn "hello world"
